
from django.urls import path, re_path

from .views import ProductsViewSet

urlpatterns = [           
    path('list', ProductsViewSet.as_view({'post':'create'}), name="create_product"),
    re_path("^product/(?P<pk>[0-9a-f]+)", ProductsViewSet.as_view({"delete": "destroy"}), name="delete_product"),
]