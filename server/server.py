import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from utils.routes import (
    resolve_routes_get_customer,
    resolve_routes_post_customer,
    resolve_routes_put_customer,
    resolve_routes_delete_customer
)

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
        result = resolve_routes_post_customer(self.path, data)
        if result['status'] == 200:
            self.send_response(result['status'])
            self.send_header('localtion', result['message'])
            self.end_headers()
            self.wfile.write(json.dumps(data).encode(encoding='utf_8'))
        else:
            self.send_response(result['status'])
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(result['message'].encode(encoding='utf_8'))

    def do_PUT(self):
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(self.data_string)
        result = resolve_routes_put_customer(self.path, data)
        self.send_response(200)
        self.send_header('localtion', result['message'])
        self.end_headers()
        self.wfile.write(json.dumps(data).encode(encoding='utf_8'))

    def do_DELETE(self):
        result = resolve_routes_delete_customer(self.path)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(result['message'].encode('utf-8')))

httpd = HTTPServer(('localhost', 8080), Server)
print('\nListening at 8080\n\t.... \nWaiting for requests.')
try:
    httpd.serve_forever()
except KeyboardInterrupt:
        print('\nBye!')