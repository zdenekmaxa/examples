# -*- coding: utf-8 -*-
"""
Example webapp (deployed on Google App Engine) for Selenium tests.

"""


import json
import logging as log
import datetime

import webapp2


class RequestHandler(webapp2.RequestHandler):
    def index(self):
        msg = "current datetime: %s" % datetime.datetime.now()
        log.info(msg)
        self.response.out.write("<html><body>")
        self.response.out.write("<br /><br /><center><h3>" + msg +
                                "</h3></center>")
        form = ("<div><br />Enter numbers to sum:<br />\n" 
                "<form action=\"\" method=\"post\">\n"
                "<input type=\"text\" value=\"\" size=\"10\" name=\"x\">\n"
                "<span>+</span>\n"
                "<input type=\"text\" value=\"\" size=\"10\" name=\"y\">\n"
                "</div>\n"
                "<input type=\"submit\" value=\"Sum numbers\"></form>\n"
                "<br /><br />")
        self.response.out.write(form)
        # arguments are read out the same regardless of the method
        x = self.request.get("x", None)
        y = self.request.get("y", None)
        log.debug("entered values: x='%s' y='%s'" % (x, y))
        if x and y:
            try:
                s = int(x) + int(y)
            except ValueError:
                s = "error"
            self.response.out.write("result: %s + %s = %s" % (x, y, s))
        self.response.out.write("</body></html>")


routes = [
    webapp2.Route(r"/",
                  handler="main.RequestHandler:index",
                  name="index",
                  methods=["GET", "POST"]),
]


# application instance
app = webapp2.WSGIApplication(routes=routes, debug=True)
