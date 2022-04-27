from django.contrib import admin

# Register your models here.
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id_cat', 'nombre', 'pvp']
    


admin.site.register(Producto, ProductAdmin)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Categoria)
admin.site.register(DetVenta)
