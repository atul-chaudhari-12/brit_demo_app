
from django.urls import path

from .views import LoginFormView, LogoutView, SignUpFormView

urlpatterns = [    
    path('login', LoginFormView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('signup', SignUpFormView.as_view(), name="signup")        
]