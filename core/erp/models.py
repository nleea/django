from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime
from django.forms import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL
from core.models import BaseModel
from crum import get_current_user
# Create your models here.


class Cliente(models.Model):
    GENDER_CHOISE = [('M', 'Masculino'), ('F', 'Femenino')]
    names = models.CharField(max_length=50, verbose_name="Nombre")
    surnames = models.CharField(max_length=100, verbose_name="Apellidos")
    dni = models.CharField(max_length=11, unique=True, verbose_name="Dni")
    date_birthday = models.DateField(
        default=datetime.now, verbose_name='Fecha de nacimiento')
    direccion = models.CharField(
        max_length=150, null=True, blank=True, verbose_name='Dirección')
    gender = models.CharField(
        max_length=100, choices=GENDER_CHOISE, default='male', verbose_name='Sexo')

    def __str__(self) -> str:
        return self.names

    def toJSON(self):
        item = model_to_dict(self)
        item['gender'] = self.get_gender_display()
        item['date_birthday'] = self.date_birthday.strftime('%Y-%m-%d')
        return item

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


class Categoria(BaseModel):  # para heredar una clase abstrac que no se va a crear ua tabla pero los campos que se definieron van aparecer en la tabla que la esta heredando
    nombre = models.CharField(verbose_name="Nombre",
                              unique=True, max_length=150)
    desc = models.CharField(max_length=500, null=True,
                            blank=True, verbose_name='Description')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_create = user
            else:
                self.user_update = user
        self.modified_by = user
        return super().save(force_insert, force_update, using, update_fields)

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
    pvp = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    image = models.ImageField(verbose_name='Image',
                              upload_to='product/', blank=True, null=True)

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
