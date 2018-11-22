#Maria Alvarez Hernandez ID: 4-0239-0850
#Luis Alonso Calderon Achio ID: 1-1702-0626
#Enrique Diaz Delgado ID: 1-1725-0124
#Derian Sibaja Chavarria ID 4-0232-0842

from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self): return self.title