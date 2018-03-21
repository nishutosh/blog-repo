from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Category(models.Model):
	category=models.CharField(max_length=50,unique=True)
	slug_field_category=models.SlugField(max_length=100,blank=True)
	def save(self, *args, **kwargs):
		self.slug_field_category=slugify(self.slug_field_category)
		super(Category, self).save()


class BlogPost(models.Model):
	base_category=models.ForeignKey(Category,on_delete=models.CASCADE)
	img=models.ImageField(upload_to="BlogImages/")
	title=models.CharField(max_length=200,unique=True)
	body=models.TextField()
	author=models.CharField(max_length=30)
	date=models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering=["-date"]

class Comment(models.Model):
	user_commented=models.ForeignKey(User,on_delete=models.CASCADE)
	body=models.TextField(max_length=200)

class ContactUs(models.Model):
	pass	


# Create your models here.
