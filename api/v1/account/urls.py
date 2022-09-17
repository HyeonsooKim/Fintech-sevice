from django.urls import path, include
from rest_framework import routers
from .views import AccountAssetViewSet, StockViewSet, AccountStockViewSet, TransactionHistoryViewSet

# account_asset 목록 보여주기
router = routers.DefaultRouter()
router.register(r'account-asset', AccountAssetViewSet)
router.register(r'stock', StockViewSet)
router.register(r'account-stock', AccountStockViewSet)
router.register(r'transaction', TransactionHistoryViewSet)

urlpatterns =[
    path('', include(router.urls)),
]