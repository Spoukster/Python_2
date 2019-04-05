import sys
import json
import socket
import argparse
import time



def create_args_parser():
    parser_args = argparse.ArgumentParser()
    parser_args.add_argument('-a', default='localhost')
    parser_args.add_argument('-p', default=7777)

    return parser_args


parser = create_args_parser()
args = parser.parse_args(sys.argv[1:])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((args.a, int(args.p)))
sock.listen(5)

while True:
    client, addr = sock.accept()
    print(f'Получен запрос от {addr}')
    data = client.recv(1024)
    request = json.loads(data.decode('utf-8'))

    client_action = request.get('action')

    if client_action == 'presence':
        time_now = int(time.time())
        response_string = json.dumps(
            {
                'response': '200',
                'time': time_now,
                'alert': 'Ok'
            }
        )
    else:
        response_string = 'Action not support'

    client.send(response_string.encode('utf-8'))
    client.close()
