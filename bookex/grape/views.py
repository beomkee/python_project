from django.shortcuts import render
from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
import io
from PIL import Image
from io import *
from django.views.generic import TemplateView
from .models import GraphModel
from django.http import HttpResponse
from pylab import savefig


# Create your views here.
def start(request):
	
	function = "y = [5, 10, 7, 5, 3, 4.5, 6, 8.1] | N = len(y) | x = range(N) | width = 1/1.5 | plt.bar(x, y, width, color='blue')"
	return render(request, 'grape/start.html',{'function':function} )

def graph(request):
			
		y = [5, 10, 7, 5, 3, 4.5, 6, 8.1]
		N = len(y)
		x = range(N) 
		width = 1/1.5
		result=plt.bar(x, y, width, color="blue")
		savefig('media/image/graph.png')
				
		return render(request, 'grape/graphic.html')








		
