from django.conf import settings

import string
import random


ALIAS_MIN = getattr(settings, 'ALIAS_MIN', 6)

def keygen():
    corpus = string.ascii_lowercase + string.ascii_uppercase + string.digits + '-'
    key = ''
    for _ in range(ALIAS_MIN):
        key += random.choice(corpus)
    return key

def generate_key(instance):
    Class = instance.__class__
    while True:
        key = keygen()
        qs = Class.objects.filter(alias=key).exists()
        if not qs:
            return key
        