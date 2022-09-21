from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('account/', include('api.v1.account.urls')),
    path('user/', include('api.v1.user.urls')),
    path('asset/', include('api.v1.asset.urls')),
    path('transaction/', include('api.v1.transaction.urls')),
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]