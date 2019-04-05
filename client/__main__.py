import socket
import json
import hashlib
from datetime import datetime

socket = socket.socket()
socket.connect(('localhost', 8881))

action = input('Enter action: ')
data = input('Enter data: ')

hash_obj = hashlib.sha1()
hash_obj.update(b'secret_key')

request_string = json.dumps(
    {
        'action': action,
        'time': datetime.now().timestamp(),
        'data': data,
        'user': hash_obj.hexdigest()
    }
)

socket.send(request_string.encode('utf-8'))

while True:
    response = socket.recv(1024)

    if response:
        print(response.decode('utf-8'))
        socket.close()

        break
