from django.urls import path, include
from rest_framework import routers
from .views import AccountViewSet

# account_asset 목록 보여주기
router = routers.DefaultRouter()
router.register(r'', AccountViewSet)


urlpatterns =[
    path('', include(router.urls)),
]