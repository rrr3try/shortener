from django.urls import path
from django.contrib.auth.views import LogoutView

from auth.views import SignInView, SignUpView


app_name = "auth"
urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('sign-out/', LogoutView.as_view(), name='sign-out'),

]
