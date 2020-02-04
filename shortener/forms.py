from django import forms

from .models import ClippyURL
from django.utils.translation import gettext_lazy as _


class ClippyURLForm(forms.ModelForm):
    class Meta:
        model = ClippyURL
        fields = [
            'url',
            'alias'
        ]
        labels = {
            'url': _('Paste a long URL to shorten it'),
            'alias': _('Custom alias (optional)')
        }
        widgets = {
            'url': forms.URLInput(attrs={'placeholder': 'www.example.com'}),
            'alias': forms.TextInput(attrs={'placeholder': 'Alias', 'class':'alias label'})
        }