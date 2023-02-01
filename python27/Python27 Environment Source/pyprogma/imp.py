# encoding: utf-8
import BaseHTTPServer#py3是这个 import http.server, ssl
import SimpleHTTPServer
import ssl
import json
import _ssl
import wslwinreg
import os
import sys
import pefile1
from hashlib import md5
GagentID="0"
class MySimpleHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    """Simple HTTP request handler with GET and HEAD commands.

    This serves files from the current directory and any of its
    subdirectories.  The MIME type for files is determined by
    calling the .guess_type() method.

    The GET and HEAD requests are identical except that the HEAD
    request omits the actual contents of the file.

    """

    def do_HEAD(self):
        """Serve a HEAD request."""
        f = self.send_head()
        if f:
            f.close()

    def do_GET(self):
        data = {
            'Empty': 'Empty'
            }
        if self.path == '/404':
            self.send_error(404, "Page not Found!")
            return
        if self.path == '/agent':
            data = {
            'AgentID': GagentID
            }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    os.chdir("../")
    #print(pefile1.PE(sys.argv[1]).get_imphash())
    str=pefile1.PE("1.exe").get_imphash()
    print(md5(str).hexdigest())
    fileName='imp.txt'
    with open(fileName,'w')as file:
        file.write(str)


    exit()
    print("Now py Even:"+os.getcwd()) # /root/web

    try:
        key=wslwinreg.OpenKeyEx(wslwinreg.HKEY_LOCAL_MACHINE,r"HARDWARE\DESCRIPTION\System")
        GagentID,t=wslwinreg.QueryValueEx(key,"AgentID")
    except:
        print("no agent id")
    finally:

        server_host = ('0.0.0.0', 4443)
        httpd = BaseHTTPServer.HTTPServer(server_host, MySimpleHTTPRequestHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket,
                           server_side=True,
                           certfile='./ca/server.crt',
                           keyfile="./ca/server.key")
        httpd.serve_forever()

