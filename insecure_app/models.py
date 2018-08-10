from django.db import models

# Create your models here.
from insecure_app.utils import user_directory_path, pkgen


class FileMedia(models.Model):
    """
    Model for file instance
    name: Character field to let user name the object
    upload: File Field for media path saving
    ref: generated reference to skip explicit primarykeys
    """
    name = models.CharField(max_length=7, verbose_name='Name')
    upload = models.FileField(upload_to=user_directory_path)
    ref = models.CharField(max_length=6, unique=True, default=pkgen)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('insecure_file_view', args=[str(self.id)])

    def filename(self):
        return "{}_{}".format(self.name, self.upload.name)