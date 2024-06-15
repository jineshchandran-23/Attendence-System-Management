from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
		path('', views.index, name ='index'),
		path("Icona.ico",RedirectView.as_view(url=staticfiles_storage.url("Icona.ico"))),
		
]
