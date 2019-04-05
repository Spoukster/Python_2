import sys
import json
import socket
import time

time_now = int(time.time())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) < 3:
    sock.connect((sys.argv[1], 7777))
else:
    sock.connect((sys.argv[1], int(sys.argv[2])))

request_string = json.dumps(
    {
        'action': 'presence',
        'time': time_now,
        'type': 'status',
        'user': {
            'account_name': 'C0deMaver1ck',
            'status': 'Yep, I am here!'
        }
    }
)

sock.send(request_string.encode('utf-8'))

while True:
    response = sock.recv(1024)

    if response:
        print(response.decode('utf-8'))
        sock.close()

        break
