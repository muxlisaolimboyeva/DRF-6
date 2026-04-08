from django.shortcuts import render
from .models import Shop
from .serializers import ShopSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.
# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
