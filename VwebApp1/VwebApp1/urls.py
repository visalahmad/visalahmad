#It contains the urls of project.
from django.urls import path
from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.Home),
    path("Home", views.Home),
    path("About", views.About),
    path("Contact", views.Contact),
    path("Services", views.Services),
    
]
    