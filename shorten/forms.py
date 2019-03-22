from django import forms

from .validators import validate_url


class SubmitURLForm(forms.Form):
    url = forms.CharField(label='',
                          validators=[validate_url],
                          widget=forms.TextInput(
                              attrs={
                                  'placeholder': 'Paste any long URL',
                                  'class': 'form-control',
                              }
                            )
                          )
