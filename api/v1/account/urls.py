from django.urls import path, include
from rest_framework import routers
from .views import AccountViewSet, AccountAssetViewSet

# account_asset 목록 보여주기
router = routers.DefaultRouter()
# router.register(r'', AccountViewSet)
# router.register(r'assets', AccountAssetViewSet, basename='account-assets')

urlpatterns =[
    path('<int:pk>', AccountViewSet.as_view()),
    path('<int:pk>/assets', AccountAssetViewSet.as_view())
]