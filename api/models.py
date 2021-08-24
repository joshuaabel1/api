from django.db import models


# Create your models here.
from django.contrib.auth.models import AbstractBaseUser



class Usuarios(AbstractBaseUser):
    
    nombre= models.CharField('nombre', blank=True, max_length=50, null=True)
    username= models.CharField('nombre de usuario', unique=True, max_length=50, null=True)
    password= models.CharField('Contraseña', null=True, max_length=50)
    perfil= models.ImageField('imagen de perfil', upload_to='img/', height_field=None, width_field=None,max_length=200 )
    telefono= models.CharField('numero telefonico', max_length=20, null=True)
    email= models.EmailField('correo de usuario', blank=True, max_length=50, null=True )
    linkedin= models.CharField('linkedin', unique=True, max_length=200)
    instagram=models.CharField('instagram', unique=True, max_length=200)
    github=models.CharField('github', unique=True, max_length=200)


    USERNAME_FIELD='username'
    REQUIRED_FIELD=['email', 'nombre']




    def __str__(self):
        return f'{self.nombre}, {self.password}'