import http.server
import socketserver
import ssl

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
certfile = 'server.pem'  # Path to your SSL certificate file
keyfile = 'server.key'   # Path to your SSL private key file

# Create the SSL context
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)

# Create the server instance
server = socketserver.TCPServer((host, port), handler)
server.socket = ssl_context.wrap_socket(server.socket)

# Start the server
print(f"Server running at {host}:{port}")
server.serve_forever()
