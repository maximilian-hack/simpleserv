import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = "files"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/trace':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            info = (
                f"Client IP: {self.client_address[0]}\n"
                f"Client Port: {self.client_address[1]}\n"
                f"Requested Path: {self.path}\n"
                f"Request Method: {self.command}\n"
                f"HTTP Version: {self.request_version}\n"
                f"User-Agent: {self.headers.get('User-Agent')}\n"
            )
            self.wfile.write(info.encode('utf-8'))
        else:
            super().do_GET()

os.chdir(DIRECTORY)

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
