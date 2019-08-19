from django.contrib import admin

from shortener import models

admin.site.register(models.ShortenedUrl)
