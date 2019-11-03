from http.server import HTTPServer, BaseHTTPRequestHandler
from database.customer_utils import resolve_routes_get_customer

class Server(BaseHTTPRequestHandler):
    
    def do_GET(self):
        result = resolve_routes_get_customer(self.path)
        if result:
            self.send_response(200)
        else:
            result = 'Not found'
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(result, 'utf-8'))

httpd = HTTPServer(('localhost', 8080), Server)
print('\nListening at 8080\n\t.... \nWaiting for requests.')
try:
    httpd.serve_forever()
except KeyboardInterrupt:
        print('\nBye!')