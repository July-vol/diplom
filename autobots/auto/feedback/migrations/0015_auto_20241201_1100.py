# Generated by Django 3.2.25 on 2024-12-01 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0014_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbacks',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={},
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='FeedBacks',
        ),
    ]