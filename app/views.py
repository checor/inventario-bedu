from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Producto, Cliente, Nota, Canasta
from .serializers import ProductoSerializer, ClienteSerializer, NotaSerializer, CanastaSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('cantidad')
    serializer_class = ProductoSerializer

class ClienteView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class NotaView(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

class CanastaView(viewsets.ModelViewSet):
    queryset = Canasta.objects.all()
    serializer_class = CanastaSerializer