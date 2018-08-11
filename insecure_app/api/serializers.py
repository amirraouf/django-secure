from rest_framework import serializers

from insecure_app.models import FileMedia


class FileMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileMedia
        fields = ['name', 'ref']
