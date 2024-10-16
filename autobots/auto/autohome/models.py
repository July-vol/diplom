from django.db import models


class Autohome(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    featured_image = models.ImageField(default="default.jpg", upload_to="projects/%Y/%m/%d")
    demo_link = models.CharField(max_length=200, blank=True)
    source_link = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)


def __str__(self):
    return self.title


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
