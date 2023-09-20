from django.urls import path
from core.erp.views.producto.views import *
from core.erp.views.dashboard.views import *

app_name = 'app'

urlpatterns = [
    # PADRON
    # path('list/', prueba),
    path('producto/list/', ProductoListView.as_view(), name='producto_list'),
<<<<<<< HEAD
    path('producto/create/', ProductoCreateView.as_view(), name='producto_create'),
=======
>>>>>>> 4a1072f9275fe6614ea2334a2d772d86181835c3

# PANEL DASHBOARD
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

]