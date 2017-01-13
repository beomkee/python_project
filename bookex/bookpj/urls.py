from django.conf.urls import url, include
from django.contrib import admin
from bookpj.views import HomeView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^bookmark/',include('bookmark.urls', namespace='bookmark')),
	url(r'^blog/', include('blog.urls', namespace='blog')),
	url(r'^upload/', include('fileUp.urls', namespace='upfile')),


] 


