import paramiko
import os
import socket
import sys
import threading
from dotenv import load_dotenv
load_dotenv()

from paramiko.channel import Channel

class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()
        print(os.getenv('SSH_USERNAME'))

    def check_channel_request(self, kind, chanid):
        if kind == 'session': 
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    
    def check_auth_password(self, username, password):
        if(username == os.getenv('SSH_USERNAME')) and (password == os.getenv('SSH_PASSWORD')):
            return paramiko.AUTH_SUCCESSFUL
        
    def check_channel_pty_request(self, channel: Channel, term: bytes, width: int, height: int, pixelwidth: int, pixelheight: int, modes: bytes) -> bool:
        return True
    
    def check_channel_shell_request(self, channel: Channel) -> bool:
        return True
        
