# python modules
import os
import tempfile
import datetime

# django modules
from django.core.validators import FileExtensionValidator
from django import forms
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

# sampleproject modules
from insecure_app.models import FileMedia


TASK_UPLOAD_FILE_TYPES = [
    'vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'csv',
    'text/csv',
    'application/vnd.ms-excel',
    'vnd.ms-excel']
MIME_UPLOAD_FILE_TYPES = [
    'plain',
    'octet-stream']

TASK_UPLOAD_FILE_MAX_SIZE = 5242880
UNICODE = set(';:></*%$.\\')


class SecureUploadForm(forms.ModelForm):
    """
    Form to handle and validate file uploading, name
    Secure file check extension, mime-type, file size
    """

    upload = forms.FileField(
        label=_('Select a file'),
        help_text='max. 42 megabytes',
        validators=(FileExtensionValidator(allowed_extensions=['xls', 'xlsx', 'csv']),)
    )

    def clean_file(self):
        """
        Function that validates the file type, file name and size
        """
        file = self.cleaned_data['upload']
        if file:
            file_type = file.content_type.split('/')[1]
            number_of_dots = len(file.name.split('.'))
            if number_of_dots != 2:
                raise forms.ValidationError(
                    _('File type is not supported'))
            try:
                filename = "".join(file.name.split('.')[:-1])
            except ValueError:
                raise forms.ValidationError(
                    _('File name is not proper'))
            if not any((c in UNICODE) for c in filename):
                if file_type in TASK_UPLOAD_FILE_TYPES:
                    if file._size > TASK_UPLOAD_FILE_MAX_SIZE:
                        raise forms.ValidationError(
                            '%s' % _('Please keep file size under 5242880'))
                    if len(file.name.split('.')[0]) > 100:
                        raise forms.ValidationError(
                            _('Filename must be less than 255 characters'))

                    if 'openxml' not in file_type:
                        raise forms.ValidationError(
                            _('File type is not supported'))
                else:
                    raise forms.ValidationError(
                        _('File type is not supported'))
            else:
                raise forms.ValidationError(
                    _('Filename should not include any unicode characters ex: :, >, <, \, /, $, * '))
            try:
                fd, tmp = tempfile.mkstemp()
                with os.fdopen(fd, 'w') as out:
                    out.write(file.read())

            finally:
                os.unlink(tmp)  # delete the temp file no matter what

        return file

    class Meta:
        model = FileMedia
        fields = ('name', 'upload')
        help_texts = {
            'upload': 'max. 42 megabytes'
        }