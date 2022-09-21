from django.urls import path, include
from rest_framework import routers
from .views import AccountListView, AccountAssetListView

# account 목록 보여주기
account_list = AccountListView.as_view({
    'get': 'list',
})

# account detail 보여주기 + 수정 + 삭제
account_detail = AccountListView.as_view({
    'get': 'retrieve',
})

urlpatterns =[
    path('', account_list),
    path('<int:pk>', account_detail),
    path('<int:pk>/assets', AccountAssetListView.as_view()),
]