# Generated by Django 5.1.2 on 2024-11-29 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_feedbacks_photo_alter_feedbacks_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedbacks',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
