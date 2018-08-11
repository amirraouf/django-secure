from django.db import models

from django.utils import timezone

from rest_framework.authtoken.models import Token

from django.conf import settings


class ExpiringToken(Token):

    """Extend Token to add an expired method."""

    class Meta(object):
        proxy = True

    def expired(self):
        """Return boolean indicating token expiration."""
        now = timezone.now()
        if self.created < now - settings.EXPIRING_TOKEN_LIFESPAN:
            return True
        return False
