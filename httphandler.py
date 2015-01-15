import os
import re

#Global Constants
HTTP1_0 = "HTTP/1.0"
HTTP1_1 = "HTTP/1.1"

class HTTPRequest:
    # Process the server request into relevant HTTP request fields
    def __init__(self, data, root):
        try:
            self.HTTP_method, self.path, self.HTTP_type = data.splitlines()[0].split()
        except IndexError as e:
            print(e)

        self.URI_path = root + self.path


class HTTPResponseHandler:

    def HTTPHeaderCreator(self):
        pass

    def BadResponse(self):
        pass


    def __init__(self, http_request):
            pass







