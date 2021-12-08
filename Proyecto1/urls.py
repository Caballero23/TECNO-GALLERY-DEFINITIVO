"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include
from vistas import views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="home"),
    path('moviles/', views.moviles ,name="moviles"),
    path('accesorios/', views.accesorios ,name="accesorios"),
    path('donde_estamos/', views.donde_estamos ,name="donde_estamos"),
    path('contact/', include('contacto.urls') ),
    path('añadir/', views.añadir ,name="añadir"),
    path('buscamoviles/', views.buscamoviles, name="buscamoviles" ),
    path('modificar/<id>/', views.modificar, name="modificar" ),
    path('eliminar/<id>/', views.eliminar, name="eliminar" ),
    path('admin/', admin.site.urls),
    

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)