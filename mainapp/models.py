from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='nombre')
    apellido = models.CharField(max_length=255, verbose_name='apellido')
    email = models.EmailField(verbose_name="email")
    password = models.CharField(max_length=10,verbose_name="password")
    user = models.ForeignKey(User, editable=False, verbose_name='Usuario', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    def __str__(self):
        return self.user

        