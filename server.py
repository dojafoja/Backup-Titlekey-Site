#!/usr/bin/env python

import os
import socket

#Python 2.7 imports
try:     
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
    import commands
    
#Python 3.x imports
except ImportError:
    from http.server import SimpleHTTPRequestHandler
    from http.server import HTTPServer
    import subprocess as commands

def get_ip_address():
    if os.name == 'posix':
        ip = commands.getoutput("hostname -I")
    elif os.name == 'nt':
        ip = socket.gethostbyname(socket.gethostname())
    else:
        ip = ''
        print('Couldn\'t get local ip')
    return ip
            

def create_server():
    HandlerClass = SimpleHTTPRequestHandler
    server = HTTPServer((get_ip_address(), 8000), HandlerClass)
    serv_info = server.socket.getsockname()
    return server, serv_info

def kill_server():
    print('SHUTTING DOWN SERVER')
    server.shutdown()
        
        
if __name__ == '__main__':
    server, serv_info = create_server()
    print('\nNOW SERVING:  {} \n\nSERVING @:  http://{}:{}'.format(os.getcwd(),serv_info[0],serv_info[1]))
    print('\nPress CTRL-C to stop this server when you are finished!')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        kill_server()
    
