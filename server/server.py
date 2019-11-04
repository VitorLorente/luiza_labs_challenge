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
        if result["status"] == 200:
            self.send_response(result["status"])
            self.send_header('Content-Type', 'application/json')
        else:
            self.send_response(result["status"])
            self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(result["data"].encode(encoding='utf_8'))

    def do_POST(self):
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(self.data_string)
        result = resolve_routes_post_customer(self.path, data)
        if result['status'] == 200:
            self.send_response(result['status'])
            self.send_header('location', result['message'])
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
        response = ''
        if result['status'] == 200:
            self.send_response(result['status'])
            self.send_header('location', result['message'])
            response = json.dumps(data).encode(encoding='utf_8')
        else:
            self.send_response(result['status'])
            self.send_header('Content-Type', 'text/html')
            response = result["message"].encode(encoding='utf_8')
        self.end_headers()
        self.wfile.write(response)

    def do_DELETE(self):
        result = resolve_routes_delete_customer(self.path)
        self.send_response(result['status'])
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(result['message'].encode('utf-8')))

def runserver(port):
    httpd = HTTPServer(('localhost', port), Server)
    print(f'\nListening at {port}\n\t.... \nWaiting for requests.')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
            print('\nBye!')