from django.urls import path
from core.erp.views.producto.views import *

app_name = 'app'

urlpatterns = [
    # PADRON
    # path('list/', prueba),
    path('producto/list/', ProductoListView.as_view(), name='producto_list')

]