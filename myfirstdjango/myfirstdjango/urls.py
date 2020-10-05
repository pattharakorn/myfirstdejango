"""myfirstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from blogs import views
from blogs import models

urlpatterns = [
    path('admin/', admin.site.urls),
    ############################ test ############################
    path('', views.hello),
    path('addPost', views.addPost),

    ############################ user ############################
    path('user/get', views.apiuserget),
    path('user/post', views.apiuserpost),
    path('user/update', views.apiuserupdate),
    path('user/delete', views.apiuserdelete),

    ############################ post ############################
    path('post/get', views.apipostget),
    path('post/post', views.apipostpost),
    path('post/update', views.apipostupdate),
    path('post/delete', views.apipostdelete),

    ########################### comment ##########################
    path('comment/get', views.apicommentget),
    path('comment/post', views.apicommentpost),
    path('comment/update', views.apicommentupdate),
    path('comment/delete', views.apicommentdelete),


    # path('testpost/<int:id>', views.FindPost.as_view())
    # path('testpost/', views.sendPost.as_view()),
    # path('eiei', views.CreatePost.as_view()),
    # path('api-auth/', include('myfirstdjango.urls'))
    # path('addUser', views.adduser)
]
