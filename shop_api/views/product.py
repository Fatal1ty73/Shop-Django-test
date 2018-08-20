from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from shop_api.models import Product
from shop_api.serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    __basic_fields = ('name', 'barcode')
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter,)
    search_fields = __basic_fields
    filter_fields = __basic_fields


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
