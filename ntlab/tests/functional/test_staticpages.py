from ntlab.tests import *

class TestStaticpagesController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='staticpages', action='index'))
        # Test response...
