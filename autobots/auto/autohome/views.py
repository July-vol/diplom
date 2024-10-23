from django.shortcuts import render

from .models import Autohome


def autohome(request):
    pg = Autohome.objects.all()
    context = {'pages': pg}
    return render(request, 'autohome/index.html', context)


def about(request):
    return render(request, 'autohome/about.html')
