import logging
import os

from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import TLS_FTPHandler


def main():
    print(os.getcwd())
    print("Please enter the path of Dir which you want to serve ")
    serveing_dir = input()

    ssl_file = os.getcwd()+'/ftps_server.pem'
    ssl_genrater = "openssl req -new -keyout "+ssl_file+" -out "+ssl_file+" -x509 -days 365 -nodes -subj '/CN=www.pubnub.com/O=PubNub/C=US'"
    os.system(ssl_genrater)
    authorizer = DummyAuthorizer()
    authorizer.add_user('root', 'testTEST123$', serveing_dir, perm='elradfmwMT')
    authorizer.add_user('test1', 'test', serveing_dir, perm='elr')
    # authorizer.add_anonymous('.')
    handler = TLS_FTPHandler
    handler.certfile = ssl_file
    handler.authorizer = authorizer
    # requires SSL for both control and data channel
    handler.tls_control_required = True
    handler.tls_data_required = True

    server = FTPServer(('', 21), handler)
    os.system("rm "+ssl_file)
    logging.basicConfig(level=logging.DEBUG)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    print("Server was closed by user.")


if __name__ == '__main__':
    main()