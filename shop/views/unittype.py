from rest_framework import generics

from shop.models import UnitType
from shop.serializers import UnitTypeSerializer


class UnitTypeList(generics.ListCreateAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer


class UnitTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer