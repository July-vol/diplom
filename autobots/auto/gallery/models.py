from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='skills/images/')


def __str__(self):
    return self.title
