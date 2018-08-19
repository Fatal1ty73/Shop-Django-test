from rest_framework import generics

from shop.models import DocItem
from shop.serializers import DocItemSerializer


class DocItemList(generics.ListCreateAPIView):
    queryset = DocItem.objects.all()
    serializer_class = DocItemSerializer


class DocItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocItem.objects.all()
    serializer_class = DocItemSerializer