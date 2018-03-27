"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('category/<slug:name>',categories,name="category"),
    path('blog/<pk>',Post,name="blog"),
    path('signup/',RegisterView.as_view(),name="signup"),
    path('auth/signin/',SignInView.as_view(),name="signin"),
    path('auth/signout/',SignOutView.as_view(),name="signout"),
    path('contact/',ContactView.as_view(),name="contact"),
    path('about/',about,name="about"),
    path('comment/<pk>',comment,name="comment"),
    path('upvote/<pk>',upvote,name="upvote")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
