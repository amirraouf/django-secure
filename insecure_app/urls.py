from django.urls import path

from insecure_app.views import (
    InSecureUserCreateView,
    InSecureUserRetrieveView,
    InSecureFileUploadView,
    InSecureFileDownloadView
)

urlpatterns = [
    path('create-user/', InSecureUserCreateView.as_view(), name='insecure_user_creation'),
    path('users/', InSecureUserRetrieveView.as_view(), name='insecure_users'),
    path('upload/', InSecureFileUploadView.as_view(), name='insecure_file_upload'),
    path('download/<int:pk>/', InSecureFileDownloadView.as_view(), name='insecure_file_view'),

]