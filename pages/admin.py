#Maria Alvarez Hernandez ID: 4-0239-0850
#Luis Alonso Calderon Achio ID: 1-1702-0626
#Enrique Diaz Delgado ID: 1-1725-0124
#Derian Sibaja Chavarria ID 4-0232-0842

from django.contrib import admin

# Register your models here.
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','update_date')
    ordering = ('title',)
    search_fields = ('title',)
	
admin.site.register(Page, PageAdmin)