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
    path('view/<str:ref>/', SecureFileView.as_view(), name='secure_file_view'),
    path('view/<str:ref>/', SecureFileView.as_view(), name='secure_file_view'),
    path('download/<str:ref>/', secure_doc_download, name='secure_file_view'),

]