from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
	url(r'^$', views.upload_file, name="upload_file"),
	url(r'^(?P<doc_id>\w+)/$',views.file_detail, name='file_detail_view'),
	url(r'^(?P<doc_id>\w+)/update/$', views.file_upload, name='update'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
