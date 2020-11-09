"""ProyectoOcasa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from mainapp import views
from django.conf import settings
import os


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name="inicio"),
    path('login/', views.login_page, name="login"),
    path('tableros/',views.tablero,name="tableros"),  
    path('logout/', views.logout_user, name="logout"),
]

#Conigurar URL para imagenes

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
