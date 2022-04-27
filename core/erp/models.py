from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime
from django.forms import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL
from os import path
# Create your models here.


class Cliente(models.Model):
    GENDER_CHOISE = [('M', 'Masculino'), ('F', 'Femenino')]
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    dni = models.CharField(max_length=11, unique=True, verbose_name="Dni")
    fecha_nac = models.DateField(
        verbose_name="Fecha De Nacimiento", default=datetime.now, blank=True)
    direccion = models.CharField(
        max_length=50, blank=True, verbose_name="Direccion")
    sexo = models.CharField(choices=GENDER_CHOISE,
                            blank=True, verbose_name="Sexo", max_length=50)

    def __str__(self) -> str:
        return self.nombre

    def toJSON(self):
        return model_to_dict(self, exclude=[''])

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Venta(models.Model):
    id_cli = models.ForeignKey(
        Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_venta = models.DateField(
        verbose_name="Fecha Venta", default=datetime.now)
    subTotal = models.DecimalField(
        max_length=12, decimal_places=2, default=0, verbose_name='Sub Total', max_digits=12)
    iva = models.FloatField(verbose_name='Iva', default=0, validators=[
                            MinValueValidator(limit_value=1)])
    total = models.FloatField(verbose_name='Total', validators=[
                              MinValueValidator(limit_value=0)], default=0)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Venta'
        ordering = ['id']


class Categoria(models.Model):
    nombre = models.CharField(verbose_name="Nombre",
                              unique=True, max_length=150)
    desc = models.CharField(max_length=500, null=True,
                            blank=True, verbose_name='Description')

    def __str__(self) -> str:
        return str(self.nombre)

    def toJSON(self):
        return model_to_dict(self, exclude=[''])

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['id']


class Producto(models.Model):
    id_cat = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, blank=True, null=True)
    nombre = models.CharField(verbose_name="Nombre",
                              unique=True, max_length=150)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    image = models.ImageField(verbose_name='Image',
                              upload_to='product/a', blank=True, null=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '/{}{}'.format(STATIC_URL, 'img/empty.png')

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = "Productos"
        ordering = ['id']


class DetVenta(models.Model):
    id_venta = models.ForeignKey(
        Venta, on_delete=models.SET_NULL, blank=True, null=True)
    id_produc = models.ForeignKey(
        Producto, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(
        validators=[MinValueValidator(limit_value=0)], verbose_name="Cantidad", default=0)
    precio = models.FloatField(default=0, validators=[
                               MinValueValidator(limit_value=0)], verbose_name="Precio")
    subTotal = models.FloatField(verbose_name="Sub Total", validators=[
                                 MinValueValidator(limit_value=0)], default=0)

    def toJSON(self):
        return model_to_dict(self, exclude=[''])

    class Meta:
        verbose_name = 'Det Venta'
        verbose_name_plural = "Det Ventas"
        ordering = ['id']
