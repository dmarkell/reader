import jinja2
import json
import logging
import os
import re
import urllib
import urllib2
import webapp2

from google.appengine.api import urlfetch

# Boilerpipe Removal and Fulltext Extraction, (c) http://www.kohlschutter.com/
ENDPOINT = "http://boilerpipe-web.appspot.com/extract?"

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
        self.text = self.request.get('text').strip()

        if self.text.startswith('http://'):
            params = "url={}&output=json".format(self.text) # not urlencoded?
            try:
                response = urlfetch.fetch(ENDPOINT + params)
                data = json.loads(response.content)['response']
                text = data['content']
                title = data['title']
                self.params['title'] = title
                if text:
                    self.text = text
                else:
                    self.params['title'] = 'No content found.'
                    self.text = None
            except:
                self.params['title'] = 'Error accessing url.'
                self.text = None

        if self.text:
            text = re.sub('\s+', ' ', self.text)
            label = u"\"{}...\"".format(text[:28])
            words = text.split(" ")
            for ix, word in enumerate(words):
                if len(word) > 15:
                    words[ix] = word[10:]
                    words.insert(ix, u"{}-".format(word[:10]))
            text = u" ".join(words)
            text = json.dumps(text)
            insert = "<script>books['user']={}</script>".format(text)
            self.params['label'] = label
            self.params['book'] = insert

        self.render("reader.html", **self.params)

app = webapp2.WSGIApplication(
    [
    ('/?.*', Reader)
    ], debug=True)

