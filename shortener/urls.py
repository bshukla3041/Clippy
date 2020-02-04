from django.urls import path, re_path

from .views import index, url_redirect

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^(?P<alias>[\w-]+)/$', url_redirect, name='alias'),
]