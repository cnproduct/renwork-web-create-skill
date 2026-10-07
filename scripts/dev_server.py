#!/usr/bin/env python3
"""Loopback-only static preview. RFQ always reports disconnected; nothing is sent."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class B2BRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Robots-Tag', 'noindex, nofollow')
        super().end_headers()

    def do_POST(self):
        self.close_connection = True
        self.send_error(503 if self.path == '/api/rfq' else 404,
                        'Preview only: inquiry service is not connected; nothing was sent')


def run_server(port=8080, directory='.'):
    root = Path(directory).resolve(strict=True)
    if not root.is_dir():
        raise ValueError('Preview root must be a directory')
    with ThreadingHTTPServer(('127.0.0.1', port), partial(B2BRequestHandler, directory=str(root))) as server:
        print(f'Preview: http://127.0.0.1:{server.server_port}; inquiry delivery NOT_CONNECTED')
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('port', nargs='?', type=int, default=8080)
    cli.add_argument('directory', nargs='?', default='.')
    args = cli.parse_args()
    try:
        run_server(args.port, args.directory)
    except (ValueError, OSError) as exc:
        cli.exit(1, f'Preview failed: {exc}\n')
