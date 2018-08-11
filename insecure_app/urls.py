from django.urls import include
from django.urls import path

from insecure_app.views import (
    InSecureUserCreateView,
    InSecureUserRetrieveView,
    InSecureFileUploadView,
    InSecureFileView,
    insecure_doc_download
)

urlpatterns = [
    path('create-user/', InSecureUserCreateView.as_view(), name='insecure_user_creation'),
    path('users/', InSecureUserRetrieveView.as_view(), name='insecure_users'),
    path('upload/', InSecureFileUploadView.as_view(), name='insecure_file_upload'),
    path('view/<int:pk>/', InSecureFileView.as_view(), name='insecure_file_view'),
    path('download/<int:pk>/', insecure_doc_download, name='insecure_file_download'),
    path('api/', include('secure_app.api.urls'))

]