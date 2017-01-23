from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
# Create your models here.

@python_2_unicode_compatible

class GraphModel(models.Model):
	title = models.CharField('TITLE',max_length=50)
	slug = models.SlugField('SLUG', unique=True, allow_unicode=True)
	graph = models.ImageField(upload_to ='image')
	modify_date = models.DateTimeField('Modify Date',auto_now=True)

	class Meta:
		verbose_name = 'graph'
		verbose_name_plural = 'graphes'
		db_table ="my_graph"
		ordering = ('-modify_date',)

	def get_absolute_url(self):
	  return reverse('blog:post_detail', args=(self.slug,))

	def __str__(self):
	  return self.title

	
