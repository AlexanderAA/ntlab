import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ntlab.lib.base import BaseController, render

log = logging.getLogger(__name__)

class IndexController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/index.mako')
        # or, return a response
        return 'Hello NTLab!'
