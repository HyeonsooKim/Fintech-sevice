from django.shortcuts import render
from .serializers import AssetInfoSerializer, AssetSerializer
from django.db.models import F
from apps.asset.models import Asset
from apps.account.models import Account
from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

class AssetViewSet(ReadOnlyModelViewSet):
    """ 보유 종목 조회 Viewset """
    # queryset = Asset.objects.all()
    # serializer_class = AssetSerializer
    def get_queryset(self):
        print("self.request: ", self.request.user, dir(self.request.user))
        account = self.request.user.account.all()[0].id
        print(account)
        assets = Asset.objects.filter(account=account).annotate(
            total=F('price') * F('count')
        )
        return assets

    def get_serializer_class(self):
        if hasattr(self, 'action') and self.action == 'retrieve':
            return None

        elif hasattr(self, 'action') and self.action == 'list':
            return AssetSerializer

    def retrieve(self, request, *args, **kwargs):
        """ 보유 종목 상세 조회는 아직 제공하지 않습니다. """
        response = {'ERROR': '올바르지 않은 접근입니다.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)
