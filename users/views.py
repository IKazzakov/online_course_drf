from django.shortcuts import render
from rest_framework import viewsets

from users.models import User
from users.serializers import AuthUserSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthUserSerializer
