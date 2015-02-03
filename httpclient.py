#!/usr/bin/env python
# coding: utf-8
# Copyright 2013 Abram Hindle
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Do not use urllib's HTTP GET and POST mechanisms.
# Write your own HTTP GET and POST
# The point is to understand what you have to send and get experience with it

import sys
import socket
import re

# you may use urllib to encode data appropriately
import urllib

# Library to parse URL for encoding.
import urlparse

def help():
    print "To use httpclient.py use the cmd: httpclient.py [GET/POST] [URL]\n"
    print "or use httpclient.py [URL] (automatically set to GET)"

class HTTPRequest(object):
    def __init__(self, code=200, body=""):
        self.code = code
        self.body = body

class HTTPClient(object):
    #def get_host_port(self,url):

    def makeSocket(self):
        #print('Making Socket...')
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #print ('Socket Created')
            return s

        except socket.error as msg:
            print ('Failed to make socket. Error code: ' + str(msg[0]) + ' , Error Message: ' + str(msg[1]))
            print ('Exiting client...')
            sys.exit();

    def connect(self, host, port):
        s = self.makeSocket()
        #print ('Connecting...')
        try:
            remote_ip = socket.gethostbyname(host)
            #print ('IP Address of ' + str(host) + ' is: ' + remote_ip)

        except socket.gaierror:
            print ('Could not resolve host: %s' % (str(host)) )
            return None

        s.connect((remote_ip, port))
        #print ('Socket connected to ' + host + ' on IP: ' + remote_ip)
        return s

    def get_code(self, data=None):
        if data:
            code = int(data.splitlines()[0].split()[1])
            #print(code)
            return code
        else:
            return 404

    def get_headers(self, data=None):        
        if data:
            data_split = data.split('\r\n')
            data_split
            header = ""
            counter = 1
            for i in data_split:
                if i == data_split[0]:
                    continue

                if i == '':
                    return counter, header

                header += i + '\r\n'
                counter += 1
        else:
            return None

    def get_body(self, data=None, args=None):
        if data:
            data_split = data.split('\r\n')
            counter, header = self.get_headers(data)

            body = ""

            for i in data_split:
                if i in data_split[0:counter]:
                    continue

                body += i + '\r\n'

            return body

        else:
            return None

    # Read everything from the socket
    def recvall(self, sock):
        buffer = bytearray()
        done = False
        while not done:
            part = sock.recv(1024)
            if (part):
                buffer.extend(part)
            else:
                done = not part
        return str(buffer)

    def findHostName(self, url):
        # Parse the URL to find Host Name for socket
        try:
            host = urlparse.urlparse(url).netloc
            return host
        except:
            return None

    def buildSendMessage(self, command="", url="", args=None):
        if command == "" or url == "":
            # Case of bad message
            print (" Message Bork'd. Don't do this. ")
            sys.exit()

        parsed_url = urlparse.urlparse(url)
       
        if parsed_url.path == '':
            path = '/'
        else:
            path = parsed_url.path

        host = parsed_url.netloc

        message = command + ' ' + path +  ' ' + 'HTTP/1.1\r\n'
        message += 'Host: ' + host + '\r\n'
   
        if command == "POST":
            message += 'Content-Type: application/x-www-form-urlencoded\r\n'
            message += 'Content-Length: ' + str(len(urllib.urlencode(args))) + '\r\n'

        message = message + '\r\n'

        print(message)
        return message


    def GET(self, url, args=None):
        host = self.findHostName(url).split(":")
        if len(host) == 2:
            sock_connection = self.connect(host[0], int(host[1]))
        else:
            sock_connection = self.connect(str(host[0]), 80)

        
        if sock_connection == None:
            code = self.get_code(None)
            body = ""
            return HTTPRequest(code, body)


        try:
            send_message = self.buildSendMessage("GET", url, args)
            sock_connection.sendall(send_message)

        except socket.error:
            print('Sending Socket Message Failed. Exiting.')
            sys.exit(1)

        return_message = self.recvall(sock_connection)

        code = self.get_code(return_message)
        body = self.get_body(return_message)
        return HTTPRequest(code, body)

    def POST(self, url, args=None):
        host = self.findHostName(url).split(":")
        if len(host) == 2:
            sock_connection = self.connect(host[0], int(host[1]))
        else:
            sock_connection = self.connect(str(host[0]), 80)

        if sock_connection == None:
            code = self.get_code(None)
            body = ""
            return HTTPRequest(code, body)

        try:
            send_message = self.buildSendMessage('GET', url, args)
            sock_connection.sendall(send_message)

        except socket.error:
            print('Sending Socket Message Failed. Exiting.')
            sys.exit(1)

        return_message = self.recvall(sock_connection)

        code = self.get_code(return_message)
        body = self.get_body(return_message, args)
        return HTTPRequest(code, body)

    def command(self, url, command="POST", args=None):
        if (command == "POST"):
            return self.POST( url, args )
            sys.exit()
        else:
            return self.GET( url, args )
            sys.exit()
    
if __name__ == "__main__":
    client = HTTPClient()
    command = "GET"
    if (len(sys.argv) <= 1):
        help()
        sys.exit(1)
    elif (len(sys.argv) == 3):
        HTTPResponse = client.command(sys.argv[2], sys.argv[1])
        print HTTPResponse
        #print HTTPResponse.code
        #print HTTPResponse.body
    else:
        HTTPResponse = client.command(sys.argv[1], command) 
        print HTTPResponse
        #print HTTPResponse.code
        #print HTTPResponse.body   
