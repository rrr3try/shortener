from django.db import models
from django.urls import reverse

from hashid_field import HashidAutoField


class ShortenedUrl(models.Model):
    id = HashidAutoField(primary_key=True, min_length=3)
    full_url = models.URLField(blank=False, max_length=1024)
    counter = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    created_by_user = models.CharField(blank=True, max_length=150)

    def get_full_url(self):
        return self.full_url

    def update_counter(self):
        self.counter += 1
        self.save()

    def get_absolute_url(self):
        # [:-1] del unnecessary /
        return reverse('shortener:resolver', args={str(self.id)})[:-1]

