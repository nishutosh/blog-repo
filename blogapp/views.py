from django.shortcuts import render
from .models import *
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from.forms import *
from django.contrib import messages

def index(request):
	blogs=BlogPost.objects.all()[0:3]
	categories=Category.objects.all()
	print (categories[0])
	context_data={"blogs":blogs,"categories":categories}
	return render(request,"index.html",context_data)

def categories(request,name):
	categories=Category.objects.all()
	category=Category.objects.get(slug_field_category=name)
	context_data={"categories":categories,"category":category}
	return render(request,"category.html",context_data)

def Post(request,pk):
    blog=BlogPost.objects.get(pk=pk)
    categories=Category.objects.all()
    context_data={"blog":blog,"categories":categories}
    return render(request,"blog.html",context_data)


class RegisterView(FormView):
   template_name="register.html"
   form_class=RegisterForm
   success_url='auth/signin/'
   def form_valid(self, form):
        user_made=User.objects.create_user(first_name=form.cleaned_data["firstname"],
        	                                last_name=form.cleaned_data["lastname"],
								        	username=form.cleaned_data["username"],
								        	password=form.cleaned_data["password"],
								        	email=form.cleaned_data["email"])
        messages.success(self.request, 'User Registered')
        return super(RegisterView, self).form_valid(form)    


# Create your views here.
