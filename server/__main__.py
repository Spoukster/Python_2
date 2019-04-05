import socket
import json
import logging
import select
from datetime import datetime

from routes import resolve
from protocol import make_400, make_404, validate_request, make_response
from handlers import handle_client_request
from settings import HOST, PORT

error_handler = logging.FileHandler('error.log')
error_handler.setLevel(logging.CRITICAL)

responses = []
connections = []

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
        connections.append(client)
        logging.info(f'Client detect {address}')

        rlist, wlist, xlist = select.select(connections, connections, [], 0)

        # response_obj = responses.pop() if responses else None

        for client in connections:

            if client in rlist:

                data = client.recv(1024)
                request = json.loads(data.decode('utf-8'))

                action_name = request.get('action')

                response = handle_client_request(request)

                if response.get('code') == 400:
                    logging.error(f'Bad request: {action_name} request: {request}')

                if response.get('code') == 200:
                    responses.append(response)

                response_string = json.dumps(response)
                client.send(response_string.encode('utf-8'))

            if client in wlist:
                if responses:
                    for conn in connections:
                        response_obj_string = json.dumps(response_obj)
                        conn.send(response_obj_string.encode('utf-8'))


except KeyboardInterrupt:
    logging.info('Shutdown server')
    sock.close()
