from rest_framework import viewsets
from .serializers import AccountAssetSerializer, StockSerializer, AccountStockSerializer, TransactionHistorySerializer
from apps.account.models import AccountAsset, Stock, AccountStock, TransactionHistory
import time

class AccountAssetViewSet(viewsets.ModelViewSet):
    """
    계좌 자산 조회 Viewset
    """
    queryset = AccountAsset.objects.all()
    serializer_class = AccountAssetSerializer

class StockViewSet(viewsets.ModelViewSet):
    """
    종목 정보 조회 Viewset
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class AccountStockViewSet(viewsets.ModelViewSet):
    """
    계좌 내 종목 보유수량 및 평가금액 조회 Viewset
    """
    queryset = AccountStock.objects.all()
    serializer_class = AccountStockSerializer

class TransactionHistoryViewSet(viewsets.ModelViewSet):
    """
    거래 내역 조회 Viewset
    """
    queryset = TransactionHistory.objects.all()
    serializer_class = TransactionHistorySerializer