from django.urls import path, include
from rest_framework import routers
from .views import UserViewset

router = routers.DefaultRouter()
router.register(r'', UserViewset, basename='users')
urlpatterns =[
    path('', include(router.urls)),
]