# Generated by Django 5.1.2 on 2024-10-16 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Autohome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('featured_image', models.ImageField(default='default.jpg', upload_to='projects/%Y/%m/%d')),
                ('demo_link', models.CharField(blank=True, max_length=200)),
                ('source_link', models.CharField(blank=True, max_length=200)),
                ('tags', models.ManyToManyField(blank=True, to='autohome.tag')),
            ],
        ),
    ]
