from http.server import HTTPServer, BaseHTTPRequestHandler
from database.customer_utils import resolve_routes_get_customer, query_post_customer
from database.database import post_customer
import json

class Server(BaseHTTPRequestHandler):
    
    def do_GET(self):
        result = resolve_routes_get_customer(self.path)
        if result:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
        else:
            result = 'Not found'
            self.send_response(404)
        self.end_headers()
        self.wfile.write(result.encode(encoding='utf_8'))

    def do_POST(self):
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        data = json.loads(self.data_string)
        redirect_path = post_customer(query_post_customer(data))

        self.send_response(200)
        self.send_header('location', redirect_path)
        self.end_headers()
        self.wfile.write(json.dumps(data).encode(encoding='utf_8'))


httpd = HTTPServer(('localhost', 8080), Server)
print('\nListening at 8080\n\t.... \nWaiting for requests.')
try:
    httpd.serve_forever()
except KeyboardInterrupt:
        print('\nBye!')