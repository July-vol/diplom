from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path(r'^about.html/', views.about, name="about"),
    path(r'^blog.html/', views.blog, name="blog"),
    path(r'^services.html/', views.services, name="services"),
    path(r'^gallery.html/', views.gallery, name="gallery"),
    path(r'^contact.html/', views.contact, name="contact"),

]
