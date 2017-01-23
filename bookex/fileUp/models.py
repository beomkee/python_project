from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.conf import settings

# Create your models here.

@python_2_unicode_compatible

class UploadFileModel(models.Model):
	title = models.CharField('title', default='', max_length=50)
	docfile = models.FileField(upload_to ='documents')
	description = models.TextField('descrption', max_length=50, blank=True)
	create_date = models.DateTimeField('Create Date',auto_now_add=True)
	modify_date = models.DateTimeField('Modify Date',auto_now=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	
	class Meta:
		verbose_name = 'document'
		verbose_name_plural = 'documents'
		db_table ="my_document"
		ordering = ('-modify_date', '-pk', )

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse_lazy('upfile:file_detail_view', kwargs={'doc_id': self.id})

	def delete(self, *args, **kwargs):
		self.fields['docfile'].required = False
		super(UploadFileModel, self).delete(*args, **kwargs)

	
		





