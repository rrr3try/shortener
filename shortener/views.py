from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import RedirectView, CreateView

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


class SignUpView(CreateView):
    template_name = 'index.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('signin')
    extra_context = {'form_button_label': 'Sign Up'}


class SignInView(LoginView):
    template_name = 'index.html'
    form_class = AuthenticationForm
    extra_context = {'form_button_label': 'Sign In'}
