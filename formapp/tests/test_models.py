# formapp/tests/test_models.py

from django.test import TestCase

from formapp.models import Data_User

class TestModels(TestCase):
    
    def testing_database_create(self):
        
        self.usuario = Data_User.objects.create(
            nombres = 'Adriana',
            apellidos = 'Rodriguez',
            correo = 'adriana.rodriguez@outlook.com',
            ciudad = 'Medellin'
        )
        
        self.assertEquals(self.usuario.nombres,'Adriana')
        self.assertEquals(self.usuario.apellidos,'Rodriguez')
        self.assertEquals(self.usuario.correo,'adriana.rodriguez@outlook.com')
        self.assertEquals(self.usuario.ciudad,'Medellin')