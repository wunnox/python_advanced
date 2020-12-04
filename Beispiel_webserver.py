#!/usr/bin/python3
##############################################
#
# Name: Beispiel_webserver.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 04.12.2020
#
# Purpose: Startet einen Python-Webserver
#
##############################################


from http.server import BaseHTTPRequestHandler, HTTPServer
import time,platform

hostName = "localost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        name=platform.node()
        willkommenstext="<p><h2>Guten Tag</h2><br>Dies ist der Webserver auf dem Node <i>"+name+"</i><p>"
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://LokalerWebserver</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes(willkommenstext, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Webserver läuft auf http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Webserver gestoppt.")
