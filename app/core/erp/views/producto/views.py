from django.contrib.auth.mixins import LoginRequiredMixin
from core.erp.mixins import *
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from core.erp.models import *
from core.erp.forms import ProductoForm

# Create your views here.
class ProductoListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Producto
    template_name = 'producto/list.html'
    permission_required = 'erp.view_producto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        return context

class ProductoCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/create.html'
    success_url = reverse_lazy('app:producto_list')
    permission_required = 'erp.add_producto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Nuevo Producto'
        context['list_url'] = reverse_lazy('app:producto_list')
        context['create_url'] = reverse_lazy('app:producto_create')
        return context