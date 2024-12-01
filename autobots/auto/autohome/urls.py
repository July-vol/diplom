from xml.etree.ElementInclude import include

from django.urls import path
from feedback.views import FeedBackView
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    path('services/', views.services, name="services"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
    path('', FeedBackView.as_view(), name='feedback_view'),
]
