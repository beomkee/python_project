from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


# Create your views here.

def profile(request, username):

	User = get_user_model()
	user = get_object_or_404(User, username = username)
	documents = user.uploadfilemodel_set.order_by('-modify_date', '-pk')

	return render(request, 'profiles/profile.html', {'current_user': user,'documents':documents,})
