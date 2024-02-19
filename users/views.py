from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from users.models import User
from users.permissions import IsUserProfile
from users.serializers import AuthUserSerializer, UserSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return AuthUserSerializer
        elif self.action == 'retrieve':
            if self.request.user == self.get_object():
                return UserSerializer
            return AuthUserSerializer
        return UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['update', 'partial_update']:
            permission_classes = [IsUserProfile]
        if self.action in ['create', 'destroy']:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
