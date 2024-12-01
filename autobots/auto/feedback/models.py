from tkinter import Image
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class FeedBack(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя", blank=True, null=True)
    email = models.EmailField(max_length=255, verbose_name="e-mail", blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name="Телефон", blank=True, null=True)
    message = models.TextField(max_length=2000, verbose_name="Сообщение", blank=True, null=True)

