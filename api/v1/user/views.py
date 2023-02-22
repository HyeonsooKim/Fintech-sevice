from .serializers import UserSerializer
from apps.user.models import User
from rest_framework.viewsets import ModelViewSet

class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

