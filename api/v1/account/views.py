from rest_framework import viewsets
from .serializers import AccountSerializer
from apps.account.models import Account
import time

class AccountViewSet(viewsets.ModelViewSet):
    """
    계좌 자산 조회 Viewset
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer