from django.db import models
from django.conf import settings
from django.urls.base import reverse

from .utils import create_shortcode
from .validators import validate_url

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)


class ClippyURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(ClippyURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=False)
        return qs


class ClippyURL(models.Model):
    url = models.CharField(max_length=200, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    active = models.BooleanField(default=True)

    objects = ClippyURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(ClippyURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        # url_path = reverse('shortcode', kwargs={'shortcode': self.shortcode})
        url_path = 'http://www.clippy.pythonanywhere.com/' + self.shortcode
        return url_path
