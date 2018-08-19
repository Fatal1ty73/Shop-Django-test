from rest_framework import serializers

from shop.models import *


class UserShopSerializer(serializers.ModelSerializer):
    documents = serializers.PrimaryKeyRelatedField(many=True, queryset=Document.objects.all())

    class Meta:
        model = UserShop
        fields = ('id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'documents')


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'


class UnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitType
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Document
        fields = '__all__'


class DocItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocItem
        fields = '__all__'
