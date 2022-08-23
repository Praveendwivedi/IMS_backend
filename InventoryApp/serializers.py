from rest_framework import serializers
from InventoryApp.models import Factories, Products


class FactoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Factories
        fields=('FactoryId','FactoryName','Location')

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'