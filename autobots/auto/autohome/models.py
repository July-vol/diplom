from django.db import models
from django.urls import reverse


class Index(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    featured_image = models.ImageField(default="default.jpg", upload_to="projects/%Y/%m/%d")
    created = models.DateTimeField(auto_now_add=True)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    anons = models.CharField(max_length=255, verbose_name='Анонс')
    description = models.TextField(blank=True, verbose_name='Статья')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Фото')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')


class Gallery(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Фото')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
