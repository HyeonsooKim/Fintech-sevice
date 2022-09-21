from django.shortcuts import render
from .serializers import AssetInfoSerializer
from django.db.models import F
from apps.asset.models import AssetInfo
from apps.account.models import Account
from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

class AssetViewSet(ReadOnlyModelViewSet):
    """ 보유 종목 조회 Viewset """
    queryset = AssetInfo.objects.all()
    serializer_class = AssetInfoSerializer