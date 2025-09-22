#!/usr/bin/env python3
"""
Simple HTTP server for serving Docsify documentation locally.
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 3000
DIRECTORY = Path(__file__).parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🚀 Serving Rose Python SDK documentation at http://localhost:{PORT}")
        print(f"📁 Serving directory: {DIRECTORY}")
        print("🛑 Press Ctrl+C to stop the server")
        
        # Open browser automatically
        webbrowser.open_new_tab(f"http://localhost:{PORT}")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Stopping server...")
            httpd.shutdown()

if __name__ == "__main__":
    main()

