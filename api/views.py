from django.shortcuts import render

# Create your views here.

from rest_framework import serializers, viewsets
from rest_framework import permissions
from .serializer import CreateUserSerializer, ListasuariosSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Usuarios




class UserViewSet(ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class= ListasuariosSerializer

    def get_queryset(self):
        return Usuarios.objects.all()



class SignUpView(CreateAPIView):
    serializer_class = CreateUserSerializer

    def get_queryset(self):
        return Usuarios.objects.all()


