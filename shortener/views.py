from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView

from shortener.models import ShortenedUrl


class URLResolver(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        shortened_url: ShortenedUrl = get_object_or_404(ShortenedUrl, pk=kwargs['pk'])
        shortened_url.update_counter()
        return shortened_url.get_full_url()
