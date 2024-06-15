"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from user import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [

	path('admin/', admin.site.urls),

	##### user related path########################## 
	path('', include('user.urls')),
	path('login/', user_view.Login, name ='login'),
	path('logout/', auth.LogoutView.as_view(template_name ='/index.html'), name ='logout'),
	path('register/', user_view.register, name ='register'),
    path('attendence/', user_view.attendence, name ='attendence'),
    path('members/', user_view.members, name ='members'),
    path('myteam/', user_view.myteam, name ='myteam'),
    path('myaccount/', user_view.myaccount, name ='myaccount'),
    path('members/', user_view.members, name ='members'),
    path('html/', user_view.html, name ='html'),
     path('About/', user_view.About, name ='About'),
      path('academics/', user_view.academics, name ='academics'),
]
