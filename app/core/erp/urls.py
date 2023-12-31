from django.urls import path
from core.erp.views.producto.views import *
from core.erp.views.dashboard.views import *

app_name = 'app'

urlpatterns = [
    # PADRON
    # path('list/', prueba),
    path('producto/list/', ProductoListView.as_view(), name='producto_list'),
    path('producto/create/', ProductoCreateView.as_view(), name='producto_create'),
    path('producto/update/<int:pk>/', ProductoUpdateView.as_view(), name='producto_update'),

    # PANEL DASHBOARD
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

]