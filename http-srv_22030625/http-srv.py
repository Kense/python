import http.server
import socketserver

# Define the request handler class
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'hello world!!!')

# Set the server configuration
host = 'localhost'
port = 8000
handler = MyHandler

# Create the server instance
server = socketserver.TCPServer((host, port), handler)

# Start the server
print(f"Server running at {host}:{port}")
server.serve_forever()
