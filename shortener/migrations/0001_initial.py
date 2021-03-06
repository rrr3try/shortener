# Generated by Django 2.2.4 on 2019-08-20 10:34

from django.db import migrations, models
import hashid_field.field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortenedUrl',
            fields=[
                ('id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=3, primary_key=True, serialize=False)),
                ('full_url', models.URLField(max_length=1024)),
                ('counter', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('created_by_user', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
