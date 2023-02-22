from .serializers import UserSerializer
from apps.user.models import User
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from rest_framework.response import Response
import time

class UserSignUpView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

