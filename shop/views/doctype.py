from rest_framework import generics

from shop.models import DocumentType
from shop.serializers import DocumentTypeSerializer


class DocumentTypeList(generics.ListCreateAPIView):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer


class DocumentTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer