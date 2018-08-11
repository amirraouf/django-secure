"""Utility views for Expiring Tokens.
Classes:
    ObtainExpiringAuthToken: View to provide tokens to clients.
"""
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from insecure_app.api.serializers import FileMediaSerializer
from secure_app.models import ExpiringToken
from secure_app.api.authentication import ExpiringTokenAuthentication



class ObtainExpiringAuthToken(ObtainAuthToken):

    """View enabling username/password exchange for expiring token."""

    model = ExpiringToken

    def post(self, request, *args, **kwargs):
        """Respond to POSTed username/password with token."""
        serializer = AuthTokenSerializer(data=request.data)

        if serializer.is_valid():
            token, _ = ExpiringToken.objects.get_or_create(
                user=serializer.validated_data['user']
            )

            if token.expired():
                # If the token is expired, generate a new one.
                token.delete()
                token = ExpiringToken.objects.create(
                    user=serializer.validated_data['user']
                )

            data = {'token': token.key}
            return Response(data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class SecureDataAPIView(APIView):
    """
    Secure api that has a token but not expiring one, so if it is known
    It will be a possible vulnerability
    The solution is Expiring Token that you should specify its life span
    """
    authentication_classes = (ExpiringTokenAuthentication, )
    renderer_classes = (JSONRenderer,)
    http_method_names = ['get', 'options']

    def get(self, request, *args, **kwargs):
        serializer = FileMediaSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

