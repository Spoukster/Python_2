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

socket.send(data.encode(''))

while True:
    response = socket.recv(1024)

    if response:
        print(response.decode())
        socket.close()

        break
