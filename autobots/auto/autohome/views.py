from django.shortcuts import render

from .models import Autohome


def index(request):
    return render(request, 'autohome/index.html')


def about(request):
    return render(request, 'autohome/about.html')


def services(request):
    return render(request, 'autohome/services.html')


def gallery(request):
    return render(request, 'autohome/gallery.html')


def footer(request):
    return render(request, 'autohome/footer.html')
