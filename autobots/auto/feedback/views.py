from .forms import FeedBackForm, FeedBacksForm
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from .models import FeedBacks, FeedBack
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages


class FeedBackView(View):
    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")


class FeedBacksView(View):
    def post(self, request):
        form = FeedBacksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")


def signupuser(request):
    if request.method == "GET":
        return render(request, 'feedback/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'feedback/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'Такое имя пользователя уже существует. Задайте другое'})
        else:
            return render(request, 'feedback/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не '
                                                                                                     'совпадают'})


@login_required
def currenttodos(request):
    posts = FeedBacks.objects.filter(user=request.user, date_completed__isnull=True)
    return render(request, 'feedback/currenttodos.html', {'post': posts})


def feedback(request):
    posts = FeedBacks.objects.all()
    return render(request, 'autohome/feedback.html', {'post': posts})


@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('feedback')


def loginuser(request):
    if request.method == "GET":
        return render(request, 'feedback/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'feedback/loginuser.html',
                          {'form': AuthenticationForm(),
                           'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('currenttodos')


@login_required
def logout_user(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def createtodo(request):
    if request.method == 'GET':
        return render(request, 'feedback/createtodo.html', {'form': FeedBacksForm()})
    else:
        try:
            form = FeedBacksForm(request.POST)
            new_feedbacks = form.save(commit=False)
            new_feedbacks.user = request.user
            new_feedbacks.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'feedback/createtodo.html',
                          {'form': FeedBacksForm(),
                           'error': 'Переданы неверные данные. Попробуйте еще раз'})


@login_required
def viewtodo(request, feedback_pk):
    feedbacks = get_object_or_404(FeedBacks, pk=feedback_pk)
    if request.method == "GET":
        form = FeedBacksForm(instance=feedbacks)
        return render(request, 'feedback/viewtodo.html', {'feedbacks': feedbacks, 'form': form})
    else:
        try:
            form = FeedBacksForm(request.POST, instance=feedbacks)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'feedback/viewtodo.html',
                          {'feedbacks': feedbacks, 'form': form, 'error': 'Неверные данные'})
