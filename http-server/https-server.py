import logging
import ssl
import os

from http.server import HTTPServer, SimpleHTTPRequestHandler

def main():
    ssl_file = os.getcwd() + '/https_server.pem'
    ssl_genrater = "openssl req -new -keyout " + ssl_file + " -out " + ssl_file + " -x509 -days 365 -nodes -subj '/CN=www.pubnub.com/O=PubNub/C=US'"
    os.system(ssl_genrater)

    httpd = HTTPServer(('', 2121), SimpleHTTPRequestHandler)

    httpd.socket = ssl.wrap_socket(httpd.socket, certfile=ssl_file, server_side=True)
    os.system("rm "+ssl_file)
    # web_dir = input(print("Please enter full path of Dir which you want to serve"))
    # print(os.getcwd()+"      pwd")
    # print(os.path.dirname(__file__) + "      __file__")
    # print(web_dir+"       web_dir")
    # os.chdir(web_dir)
    # print(os.getcwd()+"pwd after change")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    print("Server was closed by user.")

if __name__ == '__main__':
    main()






