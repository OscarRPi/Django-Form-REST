# formapp/tests/test_forms.py

from django import forms
from django.test import SimpleTestCase

from formapp.forms import DataForm

class TestForms(SimpleTestCase):
    
    def test_form_with_data(self):
        
        form = DataForm(data={
            'nombres':  'Adriana', 
            'apellidos': 'Rodriguez',
            'correo':   'adriana.rodriguez@outlook.com',
            'ciudad':   'Medellin'
        })
        
        self.assertTrue(form.is_valid())
        
    def test_form_without_data(self):
        
        form = DataForm(data={
            'nombres':  '', 
            'apellidos': '',
            'correo':   '',
            'ciudad':   ''
        })
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)
        
        