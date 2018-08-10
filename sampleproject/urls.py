"""sampleproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from insecure_app.views import CommonHomeView
from secure_app.views import protected_serve

if settings.DEBUG:
    admin_url = path('admin/', admin.site.urls)

else:
    admin_url = path('unpredictable_portal_path/', admin.site.urls)

sec_media_url = static('secure' + settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, view=protected_serve)
media_url = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('secure/', include('secure_app.urls')),
    path('insecure/', include('insecure_app.urls')),
    path('', CommonHomeView.as_view(), name='home'),
    admin_url,
] + media_url + sec_media_url
