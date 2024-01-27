
from django.urls import path, re_path

from .views import LoginFormView, AuthorizedDashboardView, SummaryPageView, LogoutView, ProductsViewSet

urlpatterns = [    
    path('login', LoginFormView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('dashboard', AuthorizedDashboardView.as_view(), name="dashboard"),
    path('summary', SummaryPageView.as_view(), name="summary"),
    path('products', ProductsViewSet.as_view({'post':'create'}), name="create_product"),
    re_path("^products/(?P<pk>[0-9a-f]+)", ProductsViewSet.as_view({"delete": "destroy"}), name="delete_product"),
]