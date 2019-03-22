from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .models import ClippyURL
from .forms import SubmitURLForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitURLForm()
        context = {
            'title': 'Clippy.co',
            'form': the_form
        }
        template = 'shorten/home.html'
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)
        context = {
            'title': 'Clippy.co',
            'form': form
        }
        template = 'shorten/home.html'
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = ClippyURL.objects.get_or_create(url=new_url)
            context = {
                'title': 'Clippy.co',
                'object': obj,
                'created': created
            }
            if created:
                template = 'shorten/success.html'
            else:
                template = 'shorten/already-exists.html'
        return render(request, template, context)


class URLRedirectView(View):
    def get(self, requests, shortcode=None, *args, **kwargs):
        qs = ClippyURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        return HttpResponseRedirect(obj.url)
