from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from .views import InSecureDataAPIView, AnotherInSecureDataAPIView


urlpatterns = [
    path('retrieve', InSecureDataAPIView.as_view()),
    path('retrieve_secure', AnotherInSecureDataAPIView.as_view()),
    path('get_token', ObtainAuthToken.as_view())
]