from django.db import models
from django.contrib.auth.models import User


class FeedBack(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя", blank=True, null=True)
    email = models.EmailField(max_length=255, verbose_name="Электронный адрес", blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name="Телефон", blank=True, null=True)
    message = models.TextField(max_length=2000, verbose_name="Сообщение", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'


class FeedBacks(models.Model):
    objects = None
    title = models.CharField(max_length=255, verbose_name="Укажите Ваше имя")
    memo = models.TextField(max_length=2000, verbose_name="Напишите отзыв")
    created = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    date_completed = models.DateTimeField(verbose_name="Дата", blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Фото')
    important = models.BooleanField(default=False,  verbose_name="Опубликовать")

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.title
