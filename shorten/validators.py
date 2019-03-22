from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(value):
    url_validator = URLValidator()
    value_1_invalid = False
    value_2_invalid = False
    try:
        url_validator(value)
    except:
        value_1_invalid = True
    value_new = 'http://' + value
    try:
        url_validator(value_new)
    except:
        value_2_invalid = True
    if value_1_invalid is True and value_2_invalid is True:
        raise ValidationError('Invalid url for this field')
    return value

