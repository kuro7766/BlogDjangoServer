import http.server
import socketserver
import os
import random
import sys
if __name__ == '__main__':
    print(sys.argv)
    PORT = 8000+random.randint(100,1000)

    web= r'E:\code\flutter\blog_project\build\web'

    web_dir = os.path.join(os.path.dirname(__file__), web)
    os.chdir(web_dir)
    print(f'http://127.0.0.1:{PORT}')
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("serving at port", PORT)
    httpd.serve_forever()