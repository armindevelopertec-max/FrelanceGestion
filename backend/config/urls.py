from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from freelance_core.views import (
    DashboardView, client_list_view, client_create_view, client_delete_view,
    client_edit_view, client_update_view,
    project_list_view, project_create_view, project_delete_view,
    project_edit_view, project_update_view,
    invoice_list_view, invoice_create_view, invoice_mark_paid_view,
    invoice_edit_view, invoice_update_view, update_settings_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('freelance_core.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', DashboardView.as_view(), name='home'),
    path('clientes/', client_list_view, name='client_list'),
    path('clientes/nuevo/', client_create_view, name='client_create'),
    path('clientes/<int:pk>/', client_delete_view, name='client_delete'),
    path('clientes/<int:pk>/editar/', client_edit_view, name='client_edit'),
    path('clientes/<int:pk>/actualizar/', client_update_view, name='client_update'),
    path('proyectos/', project_list_view, name='project_list'),
    path('proyectos/nuevo/', project_create_view, name='project_create'),
    path('proyectos/<int:pk>/', project_delete_view, name='project_delete'),
    path('proyectos/<int:pk>/editar/', project_edit_view, name='project_edit'),
    path('proyectos/<int:pk>/actualizar/', project_update_view, name='project_update'),
    path('facturas/', invoice_list_view, name='invoice_list'),
    path('facturas/nueva/', invoice_create_view, name='invoice_create'),
    path('facturas/<int:pk>/pagar/', invoice_mark_paid_view, name='invoice_mark_paid'),
    path('facturas/<int:pk>/editar/', invoice_edit_view, name='invoice_edit'),
    path('facturas/<int:pk>/actualizar/', invoice_update_view, name='invoice_update'),
    path('ajustes/actualizar/', update_settings_view, name='update_settings'),
]
