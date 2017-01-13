from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from fileUp.models import *
from django.views.generic import TemplateView, CreateView

# Create your views here.
class Fileupload(CreateView):

	model = UploadFileModel
	fields = ['title', 'docfile', 'description']
	template_name = 'fileUp/uploadfile.html'
	context_object_name = 'files'

	def upload_file(request):
		saved = False
	
		if requast.method == 'POST':
			form = UploadFileForm(request.POST, request.FILES)
			if form.is_valid():
				docfile = UploadFielModel()
				form.save()
				saved = True

				return HttpResponseRedirect("/upload/{}/",format(document.title))
	
		else:
			form = UploadFileForm()

		files = docfile.object.all()

		return render(request, 'uploadfile.html', {'files':files, 'form': form})

class FileDV(TemplateView):
	
	model = UploadFileModel
	template_name = 'fileUp/file_detail.html'



