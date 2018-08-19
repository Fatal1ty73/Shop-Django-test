from rest_framework import generics

from shop_api.models import UnitType
from shop_api.serializers import UnitTypeSerializer


class UnitTypeList(generics.ListCreateAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer


class UnitTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer