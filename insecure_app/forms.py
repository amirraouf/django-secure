from django import forms
from django.core.validators import FileExtensionValidator
from django.utils.translation import ugettext_lazy as _

from insecure_app.models import FileMedia


class UploadForm(forms.ModelForm):
    """Form to handle and validate file uploading, name, and security wise"""

    upload = forms.FileField(
        label=_('Select a file'),
        help_text='max. 42 megabytes',
        validators=(FileExtensionValidator(allowed_extensions=['xls', 'xlsx', 'csv']),)
    )
    class Meta:
        model = FileMedia
        fields = ('name', 'upload',)
