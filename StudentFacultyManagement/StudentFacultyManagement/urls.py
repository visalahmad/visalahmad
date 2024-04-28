#It contains the urls of project.
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.Home),
    path("Home", views.Home),
    path("About", views.About),
    path("Contact", views.Contact),
    path("Services", views.Services),
    re_path(r'^Test4/$', views.Test),
]
    