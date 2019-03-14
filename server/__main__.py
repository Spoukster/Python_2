import socket
import json

from routes import get_server_routes

sock = socket.socket()
sock.bind(('', 8000))
sock.listen(5)

while True:
    client, address = sock.accept()
    print(f'Client detected {address}')
    data = client.recv(1024)
    request = json.loads(
        data.decode('utf-8')
    )

    client_action = request.get('action')

    resolved_routes = list(
        filter(
            lambda itm: itm.get('action') == client_action,
            get_server_routes()
        )
    )

    route = resolved_routes[0] if resolved_routes else None

    if route:
        controller = route.get('controller')
        response_string = controller(request.get('data'))

    else:
        response_string = 'Action not supported'

    client.send(response_string.encode('utf-8'))
    client.close()
