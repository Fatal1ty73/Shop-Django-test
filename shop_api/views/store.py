from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from shop_api.models import Store
from shop_api.serializers import StoreSerializer


class StoreList(generics.ListCreateAPIView):
    __basic_fields = ('name')
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter,)
    search_fields = __basic_fields
    filter_fields = __basic_fields

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
