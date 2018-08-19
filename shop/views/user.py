from rest_framework import generics

from shop.models import UserShop
from shop.serializers import UserShopSerializer
from rest_framework import permissions

class UserList(generics.ListAPIView):
    queryset = UserShop.objects.all()
    serializer_class = UserShopSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = UserShop.objects.all()
    serializer_class = UserShopSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)