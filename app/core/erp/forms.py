from django.forms import ModelForm
from django import forms
from core.erp.models import *


class ProductoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Product Name',
                    'autocomplete': 'on',
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'placeholder': 'Stock',
                    'autocomplete': 'off',
                }
            ),
        }
