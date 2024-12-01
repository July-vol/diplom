from .forms import FeedBackForm
from django.views.generic import View
from django.shortcuts import redirect, render


class FeedBackView(View):
    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

