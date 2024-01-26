
from django.urls import path, include

from .views import LoginFormView

urlpatterns = [    
    path('login', LoginFormView.as_view())
]