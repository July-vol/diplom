from django.urls import path
from . import views

urlpatterns = [
    path('', views.autohome, name="index"),
    path('', views.about, name="about"),
    path('', views.services, name="services"),
    path('', views.gallery, name="gallery"),
    path('', views.footer, name="footer"),


]

