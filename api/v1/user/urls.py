from email.mime import base
from django.urls import path, include
from rest_framework import routers
from .views import UserRegisterView

# account_asset 목록 보여주기
router = routers.DefaultRouter()
# router.register(r'resister', UserRegisterView, basename="Register")

urlpatterns =[
    path('', include(router.urls)),
    path("register/", UserRegisterView.as_view()),
]