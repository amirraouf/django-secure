from django.urls import path

from .views import SecureDataAPIView, ObtainExpiringAuthToken


urlpatterns = [
    path('retrieve', SecureDataAPIView.as_view()),
    path('get_token', ObtainExpiringAuthToken.as_view())
]