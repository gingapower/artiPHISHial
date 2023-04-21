import http.server
import socketserver

PORT = 8000
FILE_NAME = "data.txt"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # Write the data to a file
        with open(FILE_NAME, 'a') as f:
            f.write(post_data)
        
        # Send a response back to the client
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Form submitted successfully!</h1></body></html>", "utf-8"))

Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
