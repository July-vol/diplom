# Generated by Django 5.1.2 on 2024-11-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0007_remove_feedbacks_memo_remove_feedbacks_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Напишите отзыв'),
        ),
    ]