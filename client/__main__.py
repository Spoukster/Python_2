import socket
import json

socket = socket.socket()
socket.connect(('localhost', 8000))

action = input('Enter action: ')
data = input('Enter data: ')

request_string = json.dumps(
    {
        'action': action,
        'data': data
    }
)

socket.send(request_string.encode('utf-8'))

while True:
    response = socket.recv(1024)

    if response:
        print(response.decode('utf-8'))
        socket.close()

        break
