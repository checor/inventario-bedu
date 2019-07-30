from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    razon_social = models.CharField(max_length=64)
    rfc = models.CharField(max_length=13)

    def __str__(self):
        return "{} {}".format(self.razon_social, self.rfc)

class Nota(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False)
    canasta = models.ForeignKey('Canasta', on_delete=models.CASCADE)


class Canasta(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, blank=False)
    productos = models.ManyToManyField(Producto, through='ProductoCanasta')

    def __str__(self):
        return "{} {}".format(self.cliente, self.productos)


class ProductoCanasta(models.Model):
    canasta = models.ForeignKey(Canasta, on_delete=models.CASCADE)
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)

    cantidad = models.IntegerField()    

    def __str__(self):
        return "{} {} {}".format(self.canasta, self.product, self.cantidad)