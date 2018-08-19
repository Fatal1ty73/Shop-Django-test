from rest_framework import generics

from shop_api.models import DocumentType
from shop_api.serializers import DocumentTypeSerializer


class DocumentTypeList(generics.ListCreateAPIView):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer


class DocumentTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer