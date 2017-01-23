from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
	url(r'^wcloud/$',views.wcloud_result, name='wcloud_result'),
	url(r'^topic/$', views.topic_result, name='topic_result'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
