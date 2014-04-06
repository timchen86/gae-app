import re
import webapp2
import urllib2
import datetime
from datetime import timedelta
from google.appengine.ext import db

import sys
sys.path.insert(0, 'libs')
from BeautifulSoup import BeautifulSoup 

import requests

import logging
logger = logging.getLogger(__name__)

from globals import USER_AGENT 

class mainPage(webapp2.RequestHandler):
    def post(self):
        logging.info(self.request)
        return

    def get(self):
        #self.response.write("It works!")
        headers = {'content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.2) Gecko/20100101 Firefox/10.0.2'}
        r = requests.get('https://github.com/timeline.json', headers=headers)
        self.response.write(r.json())
        return
 
application = webapp2.WSGIApplication([
    ('/', mainPage)], debug=True)
