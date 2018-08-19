from rest_framework import generics

from shop_api.models import DocItem
from shop_api.serializers import DocItemSerializer


class DocItemList(generics.ListCreateAPIView):
    queryset = DocItem.objects.all()
    serializer_class = DocItemSerializer


class DocItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocItem.objects.all()
    serializer_class = DocItemSerializer