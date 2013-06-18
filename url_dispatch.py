import webapp2
from controllers import *

app = webapp2.WSGIApplication([('/', LandingPage)
                              ], debug=True)