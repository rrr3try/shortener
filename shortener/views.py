from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import RedirectView

from shortener.forms import URLForm
from shortener.models import ShortenedUrl



class URLResolver(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        shortened_url: ShortenedUrl = get_object_or_404(ShortenedUrl, pk=kwargs['pk'])
        shortened_url.update_counter()
        return shortened_url.get_full_url()


class IndexView(View):
    template_name = "index.html"
    form_class = URLForm

    def post(self, request):
        form = self.form_class(request.POST)
        context = {}
        if form.is_valid():
            shortened_url = ShortenedUrl(full_url=form.cleaned_data['url'])
            shortened_url.save()
            context['shortened_urls'] = [shortened_url]

        context['url_form'] = URLForm()
        return render(request, self.template_name, context)

    def get(self, request):
        form = URLForm()
        context = {'url_form': form, 'shortened_urls': None}

        return render(request, self.template_name, context)
