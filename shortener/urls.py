from django.urls import path, re_path
from django.views import generic

from shortener import views

app_name = "shortener"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path(r'^(?P<pk>[^\/]+)/$', views.URLResolver.as_view(), name='resolver'),

]
