import socket
import json
import logging
from datetime import datetime

from routes import resolve
from protocol import make_400, make_404, validate_request, make_response

from settings import HOST, PORT

error_handler = logging.FileHandler('error.log')
error_handler.setLevel(logging.CRITICAL)

try:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            error_handler
        ]
    )

    sock = socket.socket()
    sock.bind((HOST, PORT))
    sock.listen(5)

    logging.info(f'Server start with host: {HOST} and port: {PORT}')

    # while True:
    #     client, address = sock.accept()
    #     print(f'Client detected {address}')
    #     data = client.recv(1024)
    #     request = json.loads(
    #         data.decode('utf-8')
    #     )
    #
    #     client_action = request.get('action')
    #
    #     resolved_routes = list(
    #         filter(
    #             lambda itm: itm.get('action') == client_action,
    #             get_server_routes()
    #         )
    #     )
    #
    #     route = resolved_routes[0] if resolved_routes else None
    #
    #     if route:
    #         controller = route.get('controller')
    #         response_string = controller(request.get('data'))
    #
    #     else:
    #         response_string = 'Action not supported'
    #
    #     client.send(response_string.encode('utf-8'))
    #     client.close()

    while True:
        client, address = sock.accept()
        logging.info(f'Client detect {address}')
        data = client.recv(1024)
        request = json.loads(data.decode('utf-8'))

        if validate_request(request):
            action_name = request.get('action')
            controller = resolve(action_name)
            if controller:
                try:
                    response = controller(request)
                except Exception as err:
                    logging.critical(err, exc_info=True)
                    response = make_response(
                        request, 500,
                        'Internal server error'
                    )
            else:
                logging.error(f'Action not found: { action_name }')
                response = make_404(request)
        else:
            response = make_400(request)

        if response.get('code') == 400:
            logging.error(f'Bad request: { action_name } request: { request }')

        response_string = json.dumps(response)
        client.send(response_string.encode('utf-8'))
        client.close()

except KeyboardInterrupt:
    logging.info('Shutdown server')
    sock.close()
