from django.conf.urls import *
from fileUp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
	url(r'^$', Fileupload.as_view(), name="up"),
	url(r'^file_list/$',FileLV.as_view(), name='file_list'),
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
