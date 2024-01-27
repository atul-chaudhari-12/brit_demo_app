from django.contrib import admin
from django.urls import path, include
from .views import VisiterRedirectionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('products/', include('products.urls')),
    path('', VisiterRedirectionView.as_view()) 
]
