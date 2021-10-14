from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_aadhaar(value):
    if len(value)>12 or len(value)<12 :
        raise ValidationError(
            _('%(value)s is not an valid aadhaar number'),
            params={'value': value},
        )
