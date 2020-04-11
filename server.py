import tornado.web
import tornado.ioloop
import config
import tornado.httpserver

from application import Application



# server starts from here
if __name__ == "__main__":
    app = Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(config.options["port"])
    httpServer.start(1)
    print("server already started on port is: " + str(config.options["port"]))
    tornado.ioloop.IOLoop.current().start() 