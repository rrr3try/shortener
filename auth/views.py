from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import views as generic_auth
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    template_name = 'index.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('auth:signin')
    # TODO: remove redundant implicit dependencies make template explicit
    extra_context = {'form_button_label': 'Sign Up'}


class SignInView(generic_auth.LoginView):
    template_name = 'index.html'
    form_class = AuthenticationForm
    # TODO: remove redundant implicit dependencies make template explicit
    extra_context = {'form_button_label': 'Sign In'}
