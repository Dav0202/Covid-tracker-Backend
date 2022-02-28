from django.contrib.auth import authenticate
from rest_framework.authtoken.views import  ObtainAuthToken
from rest_framework import generics, authentication, permissions
from rest_framework.settings import api_settings
from .serializers import UserSerializer, AuthTokenSerializer
from core import models
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self):
        return self.request.user

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = models.User.objects.all()
    
    