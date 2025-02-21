"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views 
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Cliente API URLs
    path('api/clientes/', views.showClienteView.as_view(), name='show_cliente'),
    path('api/clientes/add/', views.addClienteView.as_view(), name='add_cliente'),
    path('api/clientes/edit/<int:cliente_id>/', views.editClienteView.as_view(), name='edit_cliente'),
    path('api/clientes/delete/<int:cliente_id>/', views.removeClienteView.as_view(), name='remove_cliente'),
    path('api/clientes/check/', views.checkClienteView.as_view(), name='check_cliente'),

    # Transaction API URLs
    path('api/transactions/', views.showTransactionView.as_view(), name='show_transaction'),
    path('api/transactions/add/', views.addTransactionView.as_view(), name='add_transaction'),
    path('api/transactions/edit/<int:transaction_id>/', views.editTransactionView.as_view(), name='edit_transaction'),
    path('api/transactions/delete/<int:transaction_id>/', views.removeTransactionView.as_view(), name='remove_transaction'),
    path('api/transactions/check/', views.checkTransactionView.as_view(), name='check_transaction'),

]
