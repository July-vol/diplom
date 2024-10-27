from django.shortcuts import render
from .models import Blog, Gallery, ContactForm


def index(request):
    return render(request, 'autohome/index.html')


def about(request):
    return render(request, 'autohome/about.html')


def services(request):
    return render(request, 'autohome/services.html')


def blog(request):
    news = Blog.objects.all()
    return render(request, 'autohome/blog.html', {'news': news})


def gallery(request):
    pics = Gallery.objects.all()
    return render(request, 'autohome/gallery.html', {'pics': pics})


def contact(request):
    context = {}
    if request.method == 'POST':
        pass
    else:
        form = ContactForm()
        context['form'] = form
    return render(request, 'autohome/contact.html')
