#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RenWork Web Create Skill · Local Development & RFQ Server
Serves static pages with accurate MIME types and handles test B2B RFQ submissions.
"""

import sys, os, http.server, socketserver, json

class B2BRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def do_POST(self):
        if self.path == '/api/rfq':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode('utf-8')
            print(f"[B2B RFQ Server] Received inquiry payload:\n{body}")
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'success', 'message': 'RFQ recorded'}).encode('utf-8'))
        else:
            self.send_error(404, 'Endpoint not found')

def run_server(port=8080, directory='xhplasticlife-clone'):
    os.chdir(directory)
    handler = B2BRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"[Dev Server] Serving at http://localhost:{port}")
        print(f"[Dev Server] Root directory: {os.path.abspath(directory)}")
        print("Press Ctrl+C to terminate.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[Dev Server] Shutting down.")

if __name__ == '__main__':
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    d = sys.argv[2] if len(sys.argv) > 2 else 'xhplasticlife-clone'
    run_server(p, d)
