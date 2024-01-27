
from django.urls import path, re_path

from .views import AuthorizedDashboardView, SummaryPageView

urlpatterns = [       
    path('details', AuthorizedDashboardView.as_view(), name="dashboard"),
    path('summary', SummaryPageView.as_view(), name="summary"),    
]