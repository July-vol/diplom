from django.shortcuts import render
from .models import Main
from django.db.backends.base.base import BaseDatabaseWrapper


def main(request):
    pg = Main.objects.all()
    context = {'pages': pg}
    return render(request, 'autohome/main.html', context)
