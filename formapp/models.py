# formapp/models.py

from django.db import models

from django.core.validators import RegexValidator

class Data_User(models.Model):
	
    alpha = RegexValidator(r'^[a-zA-Z ]*$', 'Only alpha characters are allowed.')
    
    id_usuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50, null = False,validators=[alpha], default = "")
    apellidos = models.CharField(max_length=50, null = False,validators=[alpha], default = "")
    correo = models.EmailField(null = False, default = "")
    ciudad = models.CharField(max_length=50, null = False,validators=[alpha], default = "")
    
    def __str__(self):
        txt = "{0} - {1} {2} ({3})"
        return txt.format(self.id_usuario,self.nombres,self.apellidos,self.correo)