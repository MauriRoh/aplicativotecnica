from django.contrib import admin
from core.erp.models import *

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'desc',
    )
    # Buscador
admin.site.register(Categoria, CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cat',
        'stock',
    )
    # Buscador
admin.site.register(Producto, ProductoAdmin)