from django.urls import path, re_path
from django.views import generic

from shortener import views

app_name = "shortener"
urlpatterns = [
    path('', generic.TemplateView.as_view(template_name="index.html")),
    re_path(r'^(?P<pk>[^\/]+)/$', views.URLResolver.as_view()),

]
