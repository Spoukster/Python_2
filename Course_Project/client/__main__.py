import sys
import json
import socket
import time

time = int(time.time())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) < 3:
    sock.connect(sys.argv[1], 7777)
else:
    sock.connect(sys.argv[1], sys.argv[2])

request_string = json.loads(
    {
        'action': 'presence',
        'time': time,
        'type': 'status',
        'user': {
            'account_name': 'C0deMaver1ck',
            'status': 'Yep, I am here!'
        }
    }
)
