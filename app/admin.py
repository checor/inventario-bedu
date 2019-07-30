from django.contrib import admin
from .models import  Producto, Cliente, Nota, Canasta, ProductoCanasta

# Register your models here.
admin.site.register([
    Producto,
    Cliente,
    Nota,
    Canasta,
    ProductoCanasta
])