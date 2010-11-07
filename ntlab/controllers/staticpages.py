import logging
from pymongo.objectid import ObjectId

from pylons import config
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ntlab.lib.base import BaseController, render

app_globals = config['pylons.app_globals']
log = logging.getLogger('staticpages')

class StaticpagesController(BaseController):

    def view(self, page_url):
        page = app_globals.mongo.ntlab.staticpages.find_one({'page_url': page_url})
        if page is None:
            abort(404, 'No such page')
        c.page = page
        return str(page)
    
    def edit(self):
        # Return a rendered template
        #return render('/staticpages.mako')
        # or, return a response
        return render('/staticpages/edit.mako')
    
    def save(self):
        page = {}
        for parm in ['_id', 'page_url', 'page_title', 'page_body', 'page_enabled']:
            page[parm] = request.POST.get(parm)
            
        if (page['_id'] in [None, '']) or not app_globals.mongo.ntlab.staticpages.find_one({'_id': ObjectId(page['_id'])}):
            if app_globals.mongo.ntlab.staticpages.find_one({'page_url': page['page_url']}):
                abort(500, 'Page with given URL exists already')
            # no such page
            del page['_id']
            page['_id'] = app_globals.mongo.ntlab.staticpages.insert(page)
            raise redirect('/%s' % page['page_url'])
            
        
        