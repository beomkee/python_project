from django.contrib import admin
from grape.models import *

# Register your models here.

class GraphModelAdmin(admin.ModelAdmin):
	list_display = ('graph',)
	prepopulated_fields = {'slug':('title',)}


admin.site.register(GraphModel, GraphModelAdmin)
