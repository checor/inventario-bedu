from rest_framework import serializers

from .models import Canasta, Cliente, Nota, Producto, ProductoCanasta

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['razon_social', 'rfc']

class CanastaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Canasta
        fields = ['cliente', 'productos']

class NotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nota
        fields = ['cliente', 'canasta']

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'cantidad']