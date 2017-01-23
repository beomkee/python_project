from django.shortcuts import render,get_object_or_404, redirect
from .forms import UploadFileForm
from .models import UploadFileModel
from fileUp.models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@login_required
def upload_file(request):
		
	if request.method == "GET":
		form = UploadFileForm()

	elif request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)

		if form.is_valid():
			upload_file = form.save(commit=False)
			upload_file.user = request.user
			upload_file.save()

			return redirect(upload_file.get_absolute_url())
		
	return render(request, 'fileUp/uploadfile.html', {'form': form},)

def file_detail(request, doc_id):

	document = get_object_or_404(UploadFileModel, pk=doc_id)
	
	return render(request, 'fileUp/file_detail.html', {'document':document},)

def file_upload(request):

	document = get_object_or_404(UploadFileModel)
	
	return render(request, 'fileUp/upload.html', {'document':document},)






