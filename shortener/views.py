from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import RedirectView

from shortener.forms import URLForm
from shortener.models import ShortenedUrl


class URLResolver(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        shortened_url: ShortenedUrl = get_object_or_404(ShortenedUrl, pk=kwargs['pk'])
        ShortenedUrl.objects.filter(pk=kwargs['pk']).update(counter=F('counter')+1)
        return shortened_url.get_full_url()


class IndexView(View):
    template_name = "index.html"
    form_class = URLForm

    def post(self, request):
        form = self.form_class(request.POST)
        user = request.user.username
        context = {'form_button_label': 'shorten URL'}
        if form.is_valid():
            shortened_url = ShortenedUrl(full_url=form.cleaned_data['url'],
                                         created_by_user=user)
            shortened_url.save()
            if len(user) > 0:
                context['shortened_urls'] = ShortenedUrl.objects.all().filter(created_by_user=user).order_by('-date')
            else:
                context['shortened_urls'] = [shortened_url]
        context['form'] = URLForm()
        return render(request, self.template_name, context)

    def get(self, request):
        form = URLForm()
        context = {'form': form, 'shortened_urls': None, 'form_button_label': 'shorten URL'}
        if request.user.is_authenticated:
            user = request.user.username
            context['shortened_urls'] = ShortenedUrl.objects.all().filter(created_by_user=user).order_by('-date')
        return render(request, self.template_name, context)
