from http.server import BaseHTTPRequestHandler, HTTPServer

class LengthServiceHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/length':
            # Read the plain text input from the request body
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            input_str = post_data.decode('utf-8')  # Decode bytes to string

            # Compute the length of the string
            length = len(input_str)

            # Send response with a newline character
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write((str(length) + '\n').encode('utf-8'))  # Add newline
        else:
            self.send_error(404, 'Endpoint not found')

def run(server_class=HTTPServer, handler_class=LengthServiceHandler, port=8081):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Length Service running on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()