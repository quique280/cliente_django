#Maria Alvarez Hernandez ID: 4-0239-0850
#Luis Alonso Calderon Achio ID: 1-1702-0626
#Enrique Diaz Delgado ID: 1-1725-0124
#Derian Sibaja Chavarria ID 4-0232-0842

from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index')
    url(r'^afirmacion2$', views.index , name='afirmacion'),
    url(r'([^/]*)', views.index, name='index')
]