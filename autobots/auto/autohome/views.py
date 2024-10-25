from django.shortcuts import render

from .models import Autohome


def autohome(request):
    projects = Autohome.objects.all()
    return render(request, 'autohome/index.html', {'projects': projects})


def about(request):
    return render(request, 'autohome/about.html')


def services(request):
    return render(request, 'autohome/services.html')


def gallery(request):
    return render(request, 'autohome/gallery.html')


def footer(request):
    return render(request, 'autohome/footer.html')
