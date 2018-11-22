"""cliente_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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


Maria Alvarez Hernandez ID: 4-0239-0850
Luis Alonso Calderon Achio ID: 1-1702-0626
Enrique Diaz Delgado ID: 1-1725-0124
Derian Sibaja Chavarria ID 4-0232-0842
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('pages.urls'))
]
