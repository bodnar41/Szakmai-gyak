"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from devicemgmt import views
from django.urls import include

urlpatterns = [
    path('', views.home, name='home'),
    path('list_devices/', views.list_devices, name='list_devices'),
    path('add_devices/', views.add_devices, name='add_devices'),
    path('update_devices/<str:pk>/', views.update_devices, name="update_devices"),
    path('delete_devices/<str:pk>/', views.delete_devices, name="delete_devices"),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
]


