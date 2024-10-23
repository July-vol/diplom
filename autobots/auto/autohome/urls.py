from django.urls import path
from . import views

urlpatterns = [
    path('', views.autohome, name='index'),
    path('about/', views.about, name='about'),

]
