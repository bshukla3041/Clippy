from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import ClippyURL
from .forms import SubmitURLForm


def index_view(request, *args, **kwargs):
    form = SubmitURLForm()
    context = {
        'title': 'Clippy',
        'form': form
    }
    template = 'shorten/home.html'
    if request.method == 'POST':
        form = SubmitURLForm(request.POST)
        context = {
            'title': 'Clippy',
            'form': form
        }
        template = 'shorten/home.html'
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            if 'http' not in new_url:
                new_url = 'http://' + new_url
            qs = ClippyURL.objects.filter(url=new_url)
            if qs.count() == 0:
                obj = ClippyURL.objects.create(url=new_url)
                created = True
            else:
                obj = qs.first()
                created = False
            context = {
                'title': 'Clippy',
                'object': obj,
            }
            if created:
                template = 'shorten/success.html'
            else:
                template = 'shorten/already-exists.html'

    return render(request, template, context)


def url_redirect_view(request, shortcode=None, *args, **kwargs):
    qs = ClippyURL.objects.filter(shortcode__iexact=shortcode)
    if qs.count() != 1 and not qs.exists():
        raise Http404
    obj = qs.first()
    return HttpResponseRedirect(obj.url)