from django.db import models

from hashid_field import HashidAutoField


class ShortenedUrl(models.Model):
    id = HashidAutoField(primary_key=True, min_length=3)
    full_url = models.URLField(blank=False, max_length=1024)
    counter = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def get_full_url(self):
        return self.full_url

    def update_counter(self):
        self.counter += 1
        self.save()
