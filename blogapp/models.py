from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Category(models.Model):
	category=models.CharField(max_length=50,unique=True)
	slug_field_category=models.SlugField(max_length=100,blank=True)
	def save(self, *args, **kwargs):
		self.slug_field_category=slugify(self.slug_field_category)
		super(Category, self).save()

class Author(models.Model):
	author_user=models.ForeignKey(User,on_delete=models.CASCADE)
	description=models.CharField(max_length=200,unique=True)
	img=models.ImageField(upload_to="AuthorImages/")

class BlogPost(models.Model):
	base_category=models.ForeignKey(Category,on_delete=models.CASCADE)
	img=models.ImageField(upload_to="BlogImages/")
	upvote=models.IntegerField(default=0)
	favorite=models.BooleanField(default=False)
	title=models.CharField(max_length=200,unique=True)
	body=models.TextField()
	author=models.ForeignKey(Author,on_delete=models.CASCADE)
	date=models.DateTimeField(auto_now_add=True)
	read_time_minutes=models.IntegerField(default=0)
	class Meta:
		ordering=["-date"]

class Comment(models.Model):
	blog=models.ForeignKey(BlogPost,on_delete=models.CASCADE)
	user_commented=models.ForeignKey(User,on_delete=models.CASCADE)
	body=models.TextField(max_length=200)

class ContactUs(models.Model):
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	body=models.TextField()
	company=models.CharField(max_length=100)



# Create your models here.
