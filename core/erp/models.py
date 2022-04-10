from statistics import mode
from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator
# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
        db_table = 'type'
        ordering = ['name']


class Employee(models.Model):
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    GENDER_CHOISE = [('M', 'Masculino'), ('F', 'Femenino')]
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, verbose_name='cedula')
    date_joined = models.DateField(
        default=datetime.now, verbose_name="Fecha de registro")
    date_created = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    age = models.PositiveBigIntegerField(
        default=0, validators=[MaxValueValidator(limit_value=70)])
    salary = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True,)
    gender = models.CharField(choices=GENDER_CHOISE,
                              max_length=2, blank=True, default=None)

    def __str__(self) -> str:
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
