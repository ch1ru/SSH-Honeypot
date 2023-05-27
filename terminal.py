import paramiko
import os
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.getenv('SSH_USERNAME')
HOSTNAME = os.getenv('HOSTNAME')

class Terminal():
    def __init__(self, chan):
        self.chan = chan
        self.buff = ''
        self.terminal_start = f'{USERNAME}@{HOSTNAME}:~$ '
        self.curr_pointer = 0
        

    def start(self):
        print(f'Authenticated, got a catch from {self.chan.getpeername()}')
        self.chan.send("Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-128-generic x86_64)\r\n\r\n") # change to your platform if necessary
        self.chan.send(self.terminal_start)
        while True:
            r = self.chan.recv(8192)
            print(r)
            self.buff += r.decode()
            self.send_cmd(r)    

    def send_cmd(self, cmd):

        print(self.curr_pointer)
        print(self.buff)
        
        if(cmd == b'\x7f'): # Backspace
            self.buff = self.buff[:-1]
            print(self.buff)
            self.chan.send(cmd)
            if self.curr_pointer > 0:
                self.curr_pointer -= 1 
        elif(cmd == b'\r'):
            self.chan.send(b'\r\n')
            self.chan.send(self.terminal_start)
            self.buf = ''
            self.curr_pointer = 0
        elif(cmd == b'\x1b[D'):
            if (self.curr_pointer == 0):
                pass
            else:
                self.chan.send(cmd)
                self.curr_pointer -= 1
        elif(cmd == b'\x1b[C'): #right character
            if self.curr_pointer > len(self.buff):
                pass
            else:
                self.chan.send(cmd)
                self.curr_pointer += 1
        else:
            self.chan.send(cmd)
            self.curr_pointer += 1
    
    def send_bart(self):
        self.chan.send(b'\r\n')
        self.chan.send('                            . .  ,  ,\r\n')
        self.chan.send('                            |` \/ \/ \,\',\r\n')
        self.chan.send('                            ;          ` \/\,.\r\n')
        self.chan.send('                           :               ` \,/\r\n')
        self.chan.send('                           |                  /\r\n')
        self.chan.send('                           ;                 :\r\n')
        self.chan.send('                          :                  ;\r\n')
        self.chan.send('                          |      ,---.      /\r\n')
        self.chan.send('                         :     ,\'     `,-._ \\\r\n')
        self.chan.send('                         ;    (   o    \   `\'\r\n')
        self.chan.send('                       _:      .      ,\'  o ;\r\n')
        self.chan.send('                      /,.`      `.__,\'`-.__,\r\n')
        self.chan.send('                      \_  _               \\\r\n')
        self.chan.send('                     ,\'  / `,          `.,\'\r\n')
        self.chan.send('               ___,\'`-._ \_/ `,._        ;\r\n')
        self.chan.send('            __;_,\'      `-.`-\'./ `--.____)\r\n')
        self.chan.send('         ,-\'           _,--\^-\'\r\n')
        self.chan.send('       ,:_____      ,-\'     \\\r\n')
        self.chan.send('      (,\'     `--.  \;-._    ;\r\n')
        self.chan.send('      :    Y      `-/    `,  :\r\n')
        self.chan.send('      :    :       :     /_;\'\r\n')
        self.chan.send('      :    :       |    :\r\n')
        self.chan.send('       \    \      :    :\r\n')
        self.chan.send('        `-._ `-.__, \    `.\r\n')
        self.chan.send('           \   \  `. \     `.\r\n')
        self.chan.send('         ,-;    \---)_\ ,\',\'/\r\n')
        self.chan.send('         \_ `---\'--\'\" ,\'^-;\'\r\n')
        self.chan.send('         (_`     ---\'\" ,-\')\r\n')
        self.chan.send('         / `--.__,. ,-\'    \\\r\n')
        self.chan.send('         )-.__,-- ||___,--\' `-.\r\n')
        self.chan.send('        /._______,|__________,\'\\\r\n')
        self.chan.send('        `--.____,\'|_________,-\'\r\n')
                
        