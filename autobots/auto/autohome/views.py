from feedback.forms import FeedBackForm, FeedBacksForm
from feedback.models import FeedBacks
from .models import Blog, Gallery
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


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
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            subject = "Позвоните мне!"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Заполните все поля!')
            return redirect("autohome:index")

    form = FeedBackForm()
    return render(request, "autohome/contact.html", {'form': form})


def feedback(request):
    posts = FeedBacks.objects.all()
    return render(request, 'autohome/feedback.html', {'posts': posts})
