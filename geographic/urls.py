"""geographic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
#Function Based View
"""from countries.views import home"""
#Class Based View
"""from countries.views import HomeView"""
##Comportamiento por defecto
from countries.views import (HomeView, UniformView)

urlpatterns = [
    path('admin/', admin.site.urls),
    #Vistas basadas en Funciones (Function Based View)
    #path("", home)

    #Class Based View
    #path("", HomeView.as_view())
    ##Comportamiento por defecto
    path("", HomeView.as_view(), name="home"),
    path("uniform/", UniformView.as_view(), name="uniform"),
    path("continents/", include("continents.urls", namespace="continents")),
    path("countries/", include("countries.urls", namespace="countries"))
]
