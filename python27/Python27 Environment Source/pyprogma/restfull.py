# encoding: utf-8
import BaseHTTPServer#py3是这个 import http.server, ssl
import SimpleHTTPServer
import ssl
import json
import _ssl
import wslwinreg
import os
import sys
GagentID="0"
allowheadersset=set()
class MySimpleHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    """Simple HTTP request handler with GET and HEAD commands.

    This serves files from the current directory and any of its
    subdirectories.  The MIME type for files is determined by
    calling the .guess_type() method.

    The GET and HEAD requests are identical except that the HEAD
    request omits the actual contents of the file.

    """

    #支持跨域访问
    def crossdomai(self):
        self.send_header('vary', 'Origin, Access-Control-Request-Method, Access-Control-Request-Headers')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Methods', 'HEAD,PUT,GET,POST,DELETE')
        str=''
        for setvalue in allowheadersset:
            str+=','+setvalue
        self.send_header('Access-Control-Allow-Headers', 'Accept,Accept-Language,Authorization,Cache-Control,content-type,Keep-Alive,Origin,User-Agent,X-Requested-With'+str)
        #self.send_header('Access-Control-Expose-Headers', 'X-forwared-port, X-forwarded-host')
    def end_headers(self):
        self.crossdomai()
        BaseHTTPServer.BaseHTTPRequestHandler.end_headers(self)


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

    def do_OPTIONS(self):
        self.send_response(200)
        RequestHeaders=self.headers.getheader('Access-Control-Request-Headers')
        sets=RequestHeaders.split(',')
        for setvalue in sets:
            allowheadersset.add(setvalue)


        self.end_headers()
        #self.wfile.write(json.dumps(data).encode())
        

if __name__ == '__main__':



    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    os.chdir("../")
    print("Now py Even:"+os.getcwd()) # /root/web

    try:
        key=wslwinreg.OpenKeyEx(wslwinreg.HKEY_LOCAL_MACHINE,r"HARDWARE\DESCRIPTION\System")
        GagentID,t=wslwinreg.QueryValueEx(key,"AgentID")
    except:
        print("no agent id")
    finally:

        server_host = ('localhost', 8090)
        httpd = BaseHTTPServer.HTTPServer(server_host, MySimpleHTTPRequestHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket,
                           server_side=True,
                           certfile='./ca/server.crt',
                           keyfile="./ca/server.key")
        httpd.serve_forever()
