from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# def prueba(request):
#     data = {
#         'name' : 'Nombre Prueba'
#     }
#     return render(request, 'home.html', data)
    # return HttpResponse('Prueba de Template')

from django.views.generic import ListView, CreateView, UpdateView
from core.erp.models import *

# Create your views here.
class ProductoListView(ListView):
    model = Producto
    template_name = 'producto/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        return context