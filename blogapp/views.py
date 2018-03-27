from django.shortcuts import render,redirect
from .models import *
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

categories=Category.objects.all()
global_context={"categories":categories}
def index(request):
	blogs=BlogPost.objects.all()[0:3]
	categories=Category.objects.all()
	favs=BlogPost.objects.filter(favorite=True)
	context_data={"blogs":blogs,"favs":favs}
	context_data.update(global_context)
	
	return render(request,"index.html",context_data)

def categories(request,name):
	categories=Category.objects.all()
	category=Category.objects.get(slug_field_category=name)
	context_data={"category":category}
	context_data.update(global_context)
	return render(request,"category.html",context_data)

def Post(request,pk):
		blog=BlogPost.objects.get(pk=pk)
		trending=BlogPost.objects.order_by("-upvote")
		context_data={"blog":blog,"trending":trending}
		context_data.update(global_context)
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
	 def get_context_data(self, **kwargs):
				context = super(RegisterView, self).get_context_data(**kwargs)
				context.update(global_context)
				return context       

class SignInView(FormView):
	"""
	Login class
	"""
	template_name="login.html"
	form_class=SignInForm
	success_url="/"
	def form_valid(self,form):
				user=authenticate(self.request,username=form.cleaned_data["username"],password=form.cleaned_data["password"])
				if user is not None:
						if user.is_active:
									login(self.request,user)
									return super(SignInView, self).form_valid(form)
						else:
								 messages.error(self.request, 'Invalid username or password')
								 return redirect(reverse("signin"))
				else:
						 messages.error(self.request, 'Invalid username or password')
						 return redirect(reverse("signin"))

	def get_context_data(self, **kwargs):
				context = super(SignInView, self).get_context_data(**kwargs)
				context.update(global_context)
				return context            

class SignOutView(LoginRequiredMixin,View):
		def get(self,request):
					logout(request)
					messages.success(self.request, 'User Logged Out')
					return redirect(reverse("index"))  

class ContactView(FormView):
	 template_name="contact.html"
	 form_class=ContactForm
	 success_url='/'
	 def form_valid(self, form):
				user_made=ContactUs.objects.create( name=form.cleaned_data["name"],
											email=form.cleaned_data["email"],
											body=form.cleaned_data["body"],
											company=form.cleaned_data["company"])
				messages.success(self.request, 'Contact details sent')
				return super(ContactView, self).form_valid(form)
	 def get_context_data(self, **kwargs):
				context = super(ContactView, self).get_context_data(**kwargs)
				context.update(global_context)
				return context           


def about(request):	
	return render(request,"about.html",global_context)  


@login_required
def comment(request,pk):
	blog_post=BlogPost.objects.get(pk=pk)
	Comment.objects.create(blog=blog_post,user_commented=request.user,body=request.POST["body"])
	messages.success(request, 'comment registered')
	return redirect(reverse("blog",kwargs={"pk":blog_post.pk}))

def upvote(request,pk):
    blog_post=BlogPost.objects.get(pk=pk)
    blog_post.upvote+=1
    blog_post.save()
    return JsonResponse({"message":"UPVOTED"})


# Create your views here.
