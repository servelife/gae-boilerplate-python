import webapp2
from views import jinja_environment

class LandingPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('landing_page.html')
        variables = {}
        self.response.write(template.render(variables))