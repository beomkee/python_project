from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from fileUp.models import *
from django.views.generic import ListView, CreateView

# Create your views here.

class Fileupload(CreateView):

	model = UploadFileModel
	fields = ['title', 'docfile', 'description']
	template_name = 'fileUp/uploadfile.html'
	

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

		documents = docfile.object.all()

		return render(request, 'uploadfile.html', {'documents':documents, 'form': form})

class FileLV(ListView):
	
	model = UploadFileModel
	template_name = 'fileUp/file_list.html'



