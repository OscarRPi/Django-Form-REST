# formapp/tests/test_urls.py

from django.test import SimpleTestCase
from django.urls import reverse, resolve

from formapp.views import read,create,update,delete,edit

class TestsURls(SimpleTestCase):
    
    def test_read_url_is_resolved(self):
        url = reverse ('read')
        self.assertEquals(resolve(url).func,read)
        
    def test_create_url_is_resolved(self):
        url = reverse ('create')
        self.assertEquals(resolve(url).func,create)
        
    def test_update_url_is_resolved(self):
        url = reverse ('update', args=[0])
        self.assertEquals(resolve(url).func,update)
        
    def test_delete_url_is_resolved(self):
        url = reverse ('delete', args=[0])
        self.assertEquals(resolve(url).func,delete)
        
    def test_edit_url_is_resolved(self):
        url = reverse ('edit', args=[0])
        self.assertEquals(resolve(url).func,edit)
        
