from __future__ import unicode_literals
from django import forms
from .models import UploadFileModel

class UploadFileForm(forms.ModelForm):

	class Meta:
		model = UploadFileModel
		fields = ('title', 'docfile', 'description', )
		CHOICES = (('1', 'wcloud',), ('2', 'topic',))
	

