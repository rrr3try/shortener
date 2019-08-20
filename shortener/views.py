from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import get_object_or_404, render, redirect
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
        context = {'form_button_label': 'shorten URL'}
        if form.is_valid():
            shortened_url = ShortenedUrl(full_url=form.cleaned_data['url'])
            shortened_url.save()
            context['shortened_urls'] = [shortened_url]

        context['form'] = URLForm()
        return render(request, self.template_name, context)

    def get(self, request):
        form = URLForm()
        context = {'form': form, 'shortened_urls': None, 'form_button_label': 'shorten URL'}
        print(f"{request.user}")
        return render(request, self.template_name, context)


def auth(request, new_user=True):
    button_label = request.get_full_path()[1:-1]
    context = {'form_button_label': button_label}
    data = request.POST if request.method == 'POST' else None
    if new_user:
        form = UserCreationForm(data=data)
    else:
        form = AuthenticationForm(request=request, data=data)
    if form.is_valid():
        if new_user:
            user = form.save()
        else:
            user = form.get_user()

        login(request, user)
        return redirect('shortener:index')
    context['form'] = form.as_p()
    return render(request, 'index.html', context)
