from django.urls import include
from django.urls import path

from secure_app.views import (
    SecureUserCreateView,
    SecureFileUploadView,
    SecureFileView,
    secure_doc_download
)

urlpatterns = [
    path('create-user/', SecureUserCreateView.as_view(), name='secure_user_creation'),
    path('upload/', SecureFileUploadView.as_view(), name='secure_file_upload'),
    path('view/<ref>/', SecureFileView.as_view(), name='secure_file_view'),
    path('download/<ref>/', secure_doc_download, name='secure_file_download'),
    path('api/', include('secure_app.api.urls'))
]