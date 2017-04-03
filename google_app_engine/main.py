# -*- coding: utf-8 -*-
"""
Google Cloud Road Show demo.

Main application file.

Minimal application, routes.

"""


import json
import logging as log
import datetime

import webapp2
from google.appengine.api import users


class RequestHandler(webapp2.RequestHandler):
    def index(self):
        msg = "current datetime: %s" % datetime.datetime.now()
        log.info(msg)
        self.response.out.write("<br /><br /><center><h1>" + msg +
                                "</h1></center>")

    def greeting(self):
        resp = dict(datetime=str(datetime.datetime.now()),
                    currentuser=users.get_current_user().email())
        log.info(resp)
        # returns JSON
        self.response.headers["Content-Type"] = "application/json"
        self.response.out.write(json.dumps(resp))


routes = [
    webapp2.Route(r"/",
                  handler="main.RequestHandler:index",
                  name="index",
                  methods=["GET", ]),
    webapp2.Route(r"/greeting",
                  handler="main.RequestHandler:greeting",
                  name="greeting",
                  methods=["GET", ]),
]


# application instance
app = webapp2.WSGIApplication(routes=routes, debug=True)