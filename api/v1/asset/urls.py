from email.mime import base
from django.urls import path, include
from rest_framework import routers
from .views import AssetViewSet

# account_asset 목록 보여주기
router = routers.DefaultRouter()
router.register(r'', AssetViewSet, basename='asset')


urlpatterns =[
    path('', include(router.urls)),
]