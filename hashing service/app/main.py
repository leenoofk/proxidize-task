from http.server import BaseHTTPRequestHandler, HTTPServer
import hashlib

class HashServiceHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/hash':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            input_str = post_data.decode('utf-8') 

            sha256_hash = hashlib.sha256(input_str.encode('utf-8')).hexdigest()

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write((sha256_hash + '\n').encode('utf-8'))
        else:
            self.send_error(404, 'Endpoint not found')

def run(server_class=HTTPServer, handler_class=HashServiceHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Hashing Service running on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()