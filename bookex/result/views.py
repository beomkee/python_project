from django.shortcuts import render

# Create your views here.


def wcloud_result(request):

	return render(request, 'result/wcloud.html',)



def topic_result(request):

	return render(request, 'result/topic.html')
