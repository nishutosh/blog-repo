from django.contrib import admin
from .models import *
admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(ContactUs)
# Register your models here.
