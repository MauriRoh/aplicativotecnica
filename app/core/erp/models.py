from django.db import models
from django.forms import model_to_dict

class Categoria(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Producto(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cat = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    stock = models.IntegerField(default=0, verbose_name='Stock')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = '{} / {}'.format(self.name, self.cat.name)
        item['cat'] = self.cat.toJSON()
        return item

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

