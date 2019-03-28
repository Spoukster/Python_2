import socket
import json
import logging
import select
import threading
import collections
from datetime import datetime

from routes import resolve
from protocol import make_400, make_404, validate_request, make_response
from handlers import write_response, read_request
from settings import HOST, PORT

error_handler = logging.FileHandler('error.log')
error_handler.setLevel(logging.CRITICAL)

requests = collections.deque()
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
    sock.settimeout(0)

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
        try:
            client, address = sock.accept()
            connections.append(client)
            logging.info(f'Client detect {"%s:%s" % address}')
        except OSError:
            pass

        rlist, wlist, xlist = select.select(connections, connections, [], 0)

        for client in rlist:
            read_thread = threading.Thread(target=read_request, args=(client, requests))
            read_thread.start()

        if requests:
            request = requests.popleft()
            for client in wlist:
                write_thread = threading.Thread(target=write_response, args=(client, request))
                write_thread.start()
                logging.info(f'Response {request} handled and sended to {client.getsockname()}')




except KeyboardInterrupt:
    logging.info('Shutdown server')
    sock.close()
