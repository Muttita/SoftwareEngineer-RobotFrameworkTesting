#!/usr/bin/env python

"""Simple HTTP server for Robot Framework web testing demo."""

from os import chdir
from os.path import abspath, dirname, join
from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer

ROOT = join(dirname(abspath(__file__)), 'html')
PORT = 7272


class DemoServer(ThreadingMixIn, HTTPServer):
    allow_reuse_address = True

    def __init__(self, port=PORT):
        HTTPServer.__init__(self, ('localhost', int(port)), SimpleHTTPRequestHandler)

    def serve(self, directory=ROOT):
        chdir(directory)
        print('Demo server starting on port %d.' % self.server_address[1])
        try:
            self.serve_forever()
        except KeyboardInterrupt:
            self.server_close()
        print('Demo server stopped.')


if __name__ == '__main__':
    import sys
    try:
        server = DemoServer(*sys.argv[1:])
    except (TypeError, ValueError):
        print(__doc__)
    else:
        server.serve()
