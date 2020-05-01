# withoutt flask

from http.server import BaseHHTTPRequestHandler, HTTPServer

class HTTPServer_RequestHandleer(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)

        self.send_headeer("Content-type", "text/html")
        self.end_headers();

        self.wfile.write(b"<!DOCTYPE html>")
        self.wfile.write(b"<html lang='en'>")
        self.wfile.write(b"<head>")
        self.wfile.write(b"<title>Hello, title</title>")
        self.wfile.write(b"</head>")
        self.wfile.write(b"<body>")
        self.wfile.write(b"hello, world")
        self.wfile.write(b"</body>")
        self.wfile.write(b"</html>")

port = 8080
server_address = ("0.0.0.0", port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

httpd.serve_forever()