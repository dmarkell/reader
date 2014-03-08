import jinja2
import json
import logging
import os
import re
import webapp2

from google.appengine.api import urlfetch

# Template utils
template_dir = os.getcwd() + '/templates'
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render(self, template, **kw):
        self.write(render_str(template, **kw))

class Reader(Handler):

    def get(self):
        self.render("reader.html")

    def post(self):
        
        self.params = dict(book="")
        self.url = self.request.get('url')
        self.text = self.request.get('text').strip()

        if self.url:
            corpus = urlfetch.fetch(ENDPOINT + params).content
            # TODO
        
        if self.text:
            text = re.sub('\s+', ' ', self.text)
            title = u"\"{}...\"".format(text[:28])
            words = text.split(" ")
            for ix, word in enumerate(words):
                if len(word) > 15:
                    words[ix] = word[15:]
                    words.insert(ix, u"{}-".format(word[:15]))
            text = u" ".join(words)
            text = json.dumps(text)
            insert = "<script>books['user']={}</script>".format(text)
            self.params['title'] = title
            self.params['book'] = insert

        self.render("reader.html", **self.params)

app = webapp2.WSGIApplication(
    [
    ('/?.*', Reader)
    ], debug=True)

