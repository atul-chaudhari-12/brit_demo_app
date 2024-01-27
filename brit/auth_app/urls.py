
from django.urls import path, re_path

from .views import LoginFormView, LogoutView

urlpatterns = [    
    path('login', LoginFormView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),        
]