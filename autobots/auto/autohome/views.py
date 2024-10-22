from django.shortcuts import render

from .models import Index


def index(request):
    pg = Index.objects.all()
    context = {'pages': pg}
    return render(request, 'autohome/index.html', context)


def about(request):
    return render(request, 'autohome/about.html')
