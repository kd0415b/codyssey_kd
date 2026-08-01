from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello, Codyssey!</h1>')

httpd = HTTPServer(('0.0.0.0', 8080), Handler)
print('서버 시작: http://localhost:8080')
httpd.serve_forever()
