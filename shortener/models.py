from django.db import models

from django.conf import settings
from .utils import generate_key


ALIAS_MAX = getattr(settings, 'ALIAS_MAX', 15)

class ClippyURL(models.Model):

    url = models.URLField()
    alias = models.CharField(max_length=ALIAS_MAX, blank=True)
    is_custom_alias = models.BooleanField(default=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if self.alias is None or self.alias == '':
            self.is_custom_alias = False
            self.alias = generate_key(self)
        super(ClippyURL, self).save(*args, **kwargs)

    def get_short_url(self):
        HOST = 'http://localhost:8000/'
        url_path = HOST + self.alias
        return url_path
    