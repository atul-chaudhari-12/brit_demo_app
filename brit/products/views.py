from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from products.models import Products
from products.serializers import ProductSerializer

class ProductsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductSerializer