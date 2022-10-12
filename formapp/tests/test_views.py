# formapp/tests/test_views.py

from django.test import TestCase, Client
from django.urls import reverse

from formapp.models import Data_User

class TestViews(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        
        cls.obj_id = Data_User.objects.create(nombres="Oscar").pk
        
    def setUp(self):
        
        self.client = Client()
        
        d_u = Data_User.objects.get(id_usuario=self.obj_id)
        
        self.delete_url = reverse("delete",args=[d_u.id_usuario])
        self.create_url = reverse('create')
        self.read_url = reverse('read')
        self.edit_url = reverse('edit', args=[d_u.id_usuario])

    def test_create_view_get(self):
        
        response = self.client.get(self.create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formapp/form.html')
        
    def test_create_view_post(self):
        
        response = self.client.post(self.create_url, {
            'nombres':  'Adriana', 
            'apellidos': 'Rodriguez',
            'correo':   'adriana.rodriguez@outlook.com',
            'ciudad':   'Medellin'
        })
        
        self.assertEquals(response.status_code,302)
    
    def test_create_view_post_no_data(self):
        
        response = self.client.post(self.create_url)
        self.assertEquals(response.status_code,200)
        
    def test_read_view(self):
        
        response = self.client.get(self.read_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formapp/index.html')
    
    def test_edit_view(self):
        
        response = self.client.get(self.edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'formapp/edit.html')
        
    def test_delete_view(self):
        
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, 302)

    

    
    
    