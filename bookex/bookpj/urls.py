from django.conf.urls import url, include
from django.contrib import admin
from bookpj.views import HomeView, UserCreateView,UserCreateDoneTV
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	
	url(r'^admin/', include(admin.site.urls)),

	url(r'^accounts/', include('django.contrib.auth.urls')),
	url(r'^accounts/register/$', UserCreateView.as_view(), name = 'register'),
	url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name = 'register_done'),
	
	url(r'^user/', include('profiles.urls', namespace='profiles')),

	url(r'^$', HomeView.as_view(), name='home'),

	url(r'^upload/', include('fileUp.urls', namespace='upfile')),
	
	url(r'^result/', include('result.urls', namespace='result')),

	url(r'^python/', include('grape.urls',namespace = 'python_function')),
] 


