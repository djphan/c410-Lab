#!/usr/bin/env python

import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable() ## This line enables CGI error reporting

if __name__ == "__main__":
	server = BaseHTTPServer.HTTPServer
	handler = CGIHTTPServer.CGIHTTPRequestHandler
	server_address = ("", 8000)
	handler.cgi_directories = ["/cgi"]

	print("Starting Server")	 
	httpd = server(server_address, handler)
	httpd.serve_forever()
