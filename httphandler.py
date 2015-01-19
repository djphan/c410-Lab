# coding: utf-8
import os

# Copyright 2015 Daniel Phan
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


# HTTP Responses were formatted following the standard protocol
# Documents found at: http://www.rfc-editor.org/rfc/rfc2616.txt and
# formatted using the urllib2 library https://docs.python.org/2/howto/urllib2.html

HTTP_RESPONSES = {
    200: "OK",
    302: "Found",
    404: "Not Found",
    501: "Not Implemented"
}

MINE_TYPES = {
    "html" : "text/html",
    "css" : "text/css",
    "jpg" : "image/jpg"
}

class HTTPRequest:
    # Process the server request into relevant HTTP request fields
    def __init__(self, data, site_root):
        self.HTTP_method = ""
        self.HTTP_path = ""
        self.HTTP_type = ""
        self.response = 0

        # Only need the first line of the request
        try:
            self.HTTP_method, self.HTTP_path, self.HTTP_type = data.splitlines()[0].split()

            # Get index file if 'SITE_ROOT' is requested
            if self.HTTP_path == "/":
                self.HTTP_path = "/index.html"

            # Security checking test
            elif '/../' in self.HTTP_path:
                self.response = 404 

        except IndexError as e:
            print(e)

        self.abs_file_path = os.path.realpath(site_root + self.HTTP_path)

class HTTPResponse:
    def __init__(self, file_path, http_request):
            # Store all the fields for the relevant response
            self.HTTP_method = http_request.HTTP_method
            self.HTTP_path = http_request.HTTP_path
            self.HTTP_type = http_request.HTTP_type
            self.abs_file_path = http_request.abs_file_path
            self.response = http_request.response

    def ResponseChecker(self, file_path):
        # Trival case to handle security test
        if self.response == 404:
            return 404

        if self.HTTP_method != "GET":
            self.response = 404
            return self.response

        if self.HTTP_type != "HTTP/1.1":
            self.response = 404
            return self.response

        if self.HTTP_path == None:
            self.response = 404
            return self.response

        # Check for Invalid Paths    
        if not os.path.exists(self.abs_file_path):
            return 404

        # Handle /deep/ case
        if os.path.isdir(self.abs_file_path):
            return 302

        self.response = 200
        return self.response

    def MakeResponse(self):
        response_num = self.ResponseChecker(self.abs_file_path)
        mine_type = self.getMineType(self.abs_file_path)
        header = self.HTTPHeaderCreator(response_num, mine_type)

        if response_num == 200:
            site_file = open(self.abs_file_path, 'rb')
            site_body = site_file.read()
            return header + "\r\n" + site_body + "\r\n"

        if response_num == 302:
            deeper_path = self.abs_file_path
            if not self.abs_file_path.endswith("/"):
                deeper_path = self.abs_file_path + "/"

            deeper_path = deeper_path + "index.html"

            site_file = open(deeper_path, 'rb')
            site_body = site_file.read()
            return header + "\r\n" + site_body + "\r\n"

        if response_num == 404:
            return header + "\r\n" + "404: Not Found\r\n"

        return header + "\r\n" + "501: THIS IS A MYSTERY CATCH ALL CASE?\r\n"

    def getMineType(self, file_path):
        self.file_type = file_path.split('.')[-1]

        if self.file_type in MINE_TYPES:
            # UTF-8 encoding for html files
            if self.file_type == "html":
                return MINE_TYPES[self.file_type] + "; charset=UTF-8"

            return MINE_TYPES[self.file_type]

        else:
            # Return an html type if not in MINE_TYPES
            print("MINE_TYPES Not Covered")
            print (self.file_type)
            return "text/html" + "; charset=UTF-8"

    def HTTPHeaderCreator(self, response, mine_type, redirected_url=None):
        # Header format follows example found in HTTP lecutre notes (Part 1 and 2)
        # and follows guide lines

        # Format follows setup found in the python library BaseHTTPServer
        # (https://docs.python.org/2/library/basehttpserver.htm)
        if response in HTTP_RESPONSES:
            header = "%s %d %s\r\n" %("HTTP/1.1", response, HTTP_RESPONSES[response])

            # Extra line for redirect to access \deeper addressed by Dr. Hindle on
            # discussion fourms (https://eclass.srv.ualberta.ca/mod/forum/discuss.php?d=441938)    
            if response == 302:
                header = "%s %d Not Found!\r\n" %("HTTP/1.1", 200)
        else:
            # Use 501 error for cases not covered in HTTP_RESPONSES
            print("HTTP_RESPONSES Not Covered")
            print (response)
            header = "%s %d %s\r\n" %("HTTP/1.1", 501, HTTP_RESPONSES[501])

        header += "Connection: close\r\n"
        header += "Server: CMPUT404\r\n"
        header += "Accept-Ranges: bytes\r\n"
        header += "Content-Type: " + mine_type + "\r\n"
        return header








