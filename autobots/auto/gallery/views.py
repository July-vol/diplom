from django.shortcuts import render, get_object_or_404
from .models import Gallery


# Create your views here.


def gallery(request):
    images = Gallery.objects.order_by('-date')
    return render(request, 'gallery/gallery.html', {'image': images})
