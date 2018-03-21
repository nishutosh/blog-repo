from django.shortcuts import render
from .models import *

def index(request):
	blogs=BlogPost.objects.all()[0:3]
	categories=Category.objects.all()
	context_data={"blogs":blogs,"categories":categories}
	return render(request,"index.html",context_data)

def categories(render,name):
	pass
# Create your views here.
