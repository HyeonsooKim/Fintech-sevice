from rest_framework.viewsets import ReadOnlyModelViewSet
from django.shortcuts import get_object_or_404
from .serializers import AccountSerializer, AccountAssetSerializer, AccountDetailSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView
from apps.account.models import Account, AccountAsset
from django.db.models import Sum, F

class AccountListView(ReadOnlyModelViewSet):
    """
    계좌 자산 조회 Viewset
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    # def get_serializer_class(self):
    #     if hasattr(self, 'action') and self.action == 'retrieve':
    #         return AccountDetailSerializer

    #     elif hasattr(self, 'action') and self.action == 'list':
    #         return AccountSerializer

class AccountAssetListView(ListAPIView):
    """
    계좌 자산 조회 Viewset
    """
    serializer_class = AccountAssetSerializer
    def get_queryset(self):
        account = get_object_or_404(Account, id=self.kwargs['pk'])
        return AccountAsset.objects.filter(account=account)
    