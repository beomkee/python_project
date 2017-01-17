from django.conf.urls import url, include
from django.contrib import admin
from bookpj.views import HomeView
from django.conf.urls.static import static
from django.conf import settings
from bookpj.views import UserCreateView,UserCreateDoneTV

urlpatterns = [
	
	url(r'^admin/', include(admin.site.urls)),

	url(r'^accounts/', include('django.contrib.auth.urls', namespace ='login')),
	url(r'^accounts/register/$', UserCreateView.as_view(), name = 'register'),
	url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name = 'register_done'),

	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^upload/', include('fileUp.urls', namespace='upfile')),


] 


