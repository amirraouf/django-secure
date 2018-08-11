from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from insecure_app.api.serializers import FileMediaSerializer


class InSecureDataAPIView(APIView):
    """
    In secure api with no authentication system
    """
    renderer_classes = (JSONRenderer,)
    http_method_names = ['get', 'options']

    def get(self, request, *args, **kwargs):
        serializer = FileMediaSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class AnotherInSecureDataAPIView(APIView):
    """
    Secure api that has a token but not expiring one, so if it is known
    It will be a possible vulnerability
    The solution is Expiring Token that you should specify its life span
    """
    authentication_classes = (TokenAuthentication, )
    renderer_classes = (JSONRenderer,)
    http_method_names = ['get', 'options']

    def get(self, request, *args, **kwargs):
        serializer = FileMediaSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


