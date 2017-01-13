from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

@python_2_unicode_compatible

class UploadFileModel(models.Model):
	title = models.CharField('title', default='', max_length=50)
	docfile = models.FileField(upload_to ='doucuments')
	description = models.CharField('descrption', max_length=100, blank=True)
	create_date = models.DateTimeField('Create Date',auto_now_add=True)
	modify_date = models.DateTimeField('Modify Date',auto_now=True)
	
	class Meta:
		verbose_name = 'document'
		verbose_name_plural = 'documents'
		db_table ="my_document"

	def __str__(self):
	  return self.title

	def get_absolute_url(self):
	  return reverse('upfile:file_detail', args=(self.title,))

	def get_previous_post(self):
	  return self.get_previous_by_modify_date()

	def get_next_post(self):
	  return self.get_next_by_modify_date()

