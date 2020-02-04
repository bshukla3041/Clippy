from django.shortcuts import render
from django.http import HttpResponseRedirect , Http404

from .forms import ClippyURLForm
from .models import ClippyURL


def index(request):

    template = ''
    context = {}

    if request.method == 'POST':
        form = ClippyURLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            alias = form.cleaned_data.get('alias')
            if 'http' not in url:
                url = 'http://' + url
            obj = None
            query_set = None

            if alias is None or alias == '':
                query_set = ClippyURL.objects.filter(url=url)
                if query_set.count() == 0:
                    obj = ClippyURL.objects.create(url=url, alias=alias)
                else:
                    flag = False
                    for item in query_set:
                        if item.is_custom_alias:
                            continue
                        else:
                            obj = item
                            flag = True
                            break
                    if not flag:
                        obj = ClippyURL.objects.create(url=url, alias=alias)
            else:
                query_set = ClippyURL.objects.filter(url=url, alias=alias)
                if query_set.count() == 0:
                    query_set = ClippyURL.objects.filter(alias=alias)
                    dup_id = 0
                    while query_set.count() != 0:
                        dup_id += 1
                        _alias = alias + str(dup_id)
                        query_set = ClippyURL.objects.filter(alias=_alias)
                    if dup_id != 0:
                        alias = alias + str(dup_id)
                    obj = ClippyURL.objects.create(url=url, alias=alias)
                else:
                    obj = query_set.first()

            context = {
                'object': obj
            }
            template = 'shortener/success.html'
        else:
            raise Http404
    else:
        form = ClippyURLForm()
        context = {
            'form': form
        }
        template = 'shortener/index.html'

    return render(request, template, context)


def url_redirect(request, alias):
    query_set = ClippyURL.objects.filter(alias__iexact=alias)
    if query_set.count() == 0:
        # raise Http404
        template = 'shortener/error404.html'
        return render(request, template)
    obj = query_set.first()
    obj.clicks += 1
    obj.save()
    return HttpResponseRedirect(obj.url)

