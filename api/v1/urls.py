from django.urls import path, include

urlpatterns = [
    path('account/', include('api.v1.account.urls')),
    path('user/', include('api.v1.user.urls')),
    path('asset/', include('api.v1.asset.urls')),
]