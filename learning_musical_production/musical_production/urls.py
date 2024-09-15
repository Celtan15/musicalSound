"""musicalProduction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views as auto_views
from django.contrib.auth import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from musical_production import views

#Aquí se van a incluir todas las urls de cada una de las aplicaciones
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('template_testing/', views.templates_testing),
    path('', include('base_app.urls')),
    path('', include('interface_module_app.urls')),
    path('', include('learning_mixture_app.urls')),
    path('accounts/', include(urls)),
]