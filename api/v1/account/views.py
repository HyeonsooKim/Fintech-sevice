from rest_framework.viewsets import ReadOnlyModelViewSet
from django.shortcuts import get_object_or_404
from .serializers import AccountSerializer, AccountAssetSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView
from apps.account.models import Account, AccountAsset
import time

class AccountViewSet(RetrieveAPIView):
    """
    계좌 자산 조회 Viewset
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountAssetViewSet(ListAPIView):
    """
    계좌 자산 조회 Viewset
    """
    serializer_class = AccountAssetSerializer
    def get_queryset(self):
        # account = self.request.user.account.all()[0].id
        # print(account)
        print("1", self.request.user.is_authenticated, dir(self.request.user))
        account = get_object_or_404(Account, id=self.kwargs['pk'])
        return AccountAsset.objects.filter(account=account)
    