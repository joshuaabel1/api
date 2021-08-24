from .models import Usuarios
from rest_framework import serializers
from .hashers import MyPBKDF2PasswordHasher
from rest_framework.serializers import ModelSerializer

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = (
            
            'email',
            'linkedin',
            'perfil',
            'telefono',
            'instagram',
            'github',
        )
        
        


class ListasuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuarios
        
        fields = (
            'email',
            'linkedin',
            'perfil',
            'telefono',
            'instagram',
            'github',
        )
