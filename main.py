import paramiko
import os
import socket
import sys
import threading
from server import Server
from terminal import Terminal

from dotenv import load_dotenv
load_dotenv()

from paramiko.channel import Channel

USERNAME = os.getenv('SSH_USERNAME')
HOSTNAME = os.getenv('HOSTNAME')
CWD = os.path.dirname(os.path.realpath(__file__))
HOSTKEY = paramiko.RSAKey(filename=os.path.join(CWD, 'test_rsa.key'))
SSH_PORT = os.getenv('SSH_PORT')

while True:     
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((os.getenv('HOST'), int(SSH_PORT)))
        sock.listen(100)
        print("Listening for connection...")
        client, addr = sock.accept()
    except Exception as e:
        print("Listen Failed: ", e)
        continue
    else:
        try:
            print("Got a connection!", client, addr)

            transport = paramiko.Transport(client)
            transport.add_server_key(HOSTKEY)
            server = Server()
            transport.start_server(server=server)

            chan = transport.accept(20)
            if chan is None:
                print('No channel')
                continue

            try:
                terminal = Terminal(chan)
                terminal.start()
            except KeyboardInterrupt:
                transport.close()

            
        except Exception as e:
            print("Listen Failed: ", e)
            continue