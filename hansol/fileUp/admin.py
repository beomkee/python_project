from django.contrib import admin
from fileUp.models import *

# Register your models here.

class UploadFileModelAdmin(admin.ModelAdmin):
	model = UploadFileModel
	list_display = ('title','description','modify_date')
	list_filter = ('modify_date',)
	search_fields = ('title','description')


admin.site.register(UploadFileModel, UploadFileModelAdmin)
