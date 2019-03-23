from django.urls import path, re_path
from .views import index_view, url_redirect_view

urlpatterns = [
    path('', index_view),
    re_path(r'^(?P<shortcode>[\w-]+)/$', url_redirect_view, name='shortcode'),
]
