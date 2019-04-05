import socket
import json
import logging
from datetime import datetime

from .routes import resolve
from .protocol import make_400, make_404, validate_request, make_response

logger = logging.getLogger('default')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.FileHandler('default.log')

handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

sock = socket.socket()
sock.bind(('', 8000))
sock.listen(5)

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

try:
    while True:
        client, address = sock.accept()
        logger.debug(f'Client detect {address}')
        data = client.recv(1024)
        request = json.loads(data.decode('utf-8'))

        if validate_request(request):
            controller = resolve(request.get('action'))
            if controller:
                try:
                    response = controller(request)
                except Exception:
                    response = make_response(
                        request, 500,
                        'Internal server error'
                    )
            else:
                response = make_404(request)
        else:
            response = make_400(request)

        response_string = json.dumps(response)
        client.send(response_string.encode('utf-8'))
        client.close()

except KeyboardInterrupt:
    sock.close()
