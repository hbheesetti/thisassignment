# coding: utf-8 
import socketserver
import mimetypes
# Copyright 2023 Abram Hindle, Eddie Antonio Santos, Hari Bheesetti
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
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/


class MyWebServer(socketserver.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print ("Got a request of: %s\n" % self.data)
        self.parse_request(self.data)
        body = self.handle_req()
        res =  "HTTP/1.1 "+ str(self.status)+ "\n"+"Content-Type: "+self.mimetype+"\n"+"\n"+body+"\n"
        self.request.sendall(bytearray(res,'utf-8'))

    def parse_request(self, req):
        req = req.decode()
        lines = req.splitlines()
        arr = lines[0].split(' ')
        self.method = arr[0]
        self.path = arr[1]

    def handle_req(self):
        x = " "
        if self.method == 'GET':
            print("path:"+self.path)
            if self.path == "/" or self.path[len(self.path)-1] == '/':
                path = "www"+self.path+"index.html"
                self.status = 200
            elif self.path.endswith(".html"):
                path = "www"+self.path
                self.status = 200
            elif self.path.endswith(".css"):
                path = "www"+self.path
                self.status = 200
            else:
                path = "www"+ self.path + "/index.html"
                self.status = 301
            self.mimetype = mimetypes.guess_type(path)[0]
            try:
                file = open(path, "r")
                x = file.read()
            except FileNotFoundError as e:
                x = "404 NOT FOUND!"
                self.status = 404
                self.mimetype= " "
            except NotADirectoryError as e:
                x = "404 NOT FOUND!"
                self.status = 404
                self.mimetype= " "
            print(x)
        else:
            self.status = 405
            self.mimetype = " "
            x = "405 NOT FOUND!"
        return x

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = socketserver.TCPServer((HOST, PORT), MyWebServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
