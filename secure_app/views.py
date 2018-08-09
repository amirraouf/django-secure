from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from django.views.static import serve

from secure_app.forms import SecureUploadForm
from insecure_app.models import FileMedia


class SecureUserCreateView(LoginRequiredMixin, CreateView):
    """
    Simple view to create an Auth user using Generic CreateView
    It automatically creates an instance of model defined and generate
    a form of fields mentioned in a list using the template name

    It will create a user with plain text password (NOT HASHED ONE)
    """
    model = get_user_model()
    template_name = 'common/create.html'
    fields = ['username', 'password', 'email']
    success_url = 'insecure/users/'


class SecureUserRetrieveView(LoginRequiredMixin, TemplateView):
    """
    Retrieve users to show that passwords not hashed and are plain
    """
    extra_context = {
        'users': get_user_model().objects.all()
    }
    template_name = 'common/users.html'


class FileUploadView(LoginRequiredMixin, CreateView):
    """
    Simple view for showing insecure file upload to apply:
    OTG-BUSLOGIC-008: Unexpected uploaded file types
    OTG-BUSLOGIC-009: Test Upload of Malicious Files
    """
    template_name = 'common/file_upload.html'
    form_class = SecureUploadForm


@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    """
    Protected Serve view is a protected django static serve
    function for adding more extra security for downloading media
    to solve
    :param request: request of user
    :param path: path of the document
    :param document_root: media root directory
    :param show_indexes: This is False by default. If it's True, Django will display file listings for directories.
    :return:
    """
    try:
        if request.user.has_permission('insecure_app.can_'):
            return serve(request, path, document_root, show_indexes)
        else:
            return redirect('insecure_file_upload')
    except FileMedia.DoesNotExist:
        return serve(request, path, document_root, show_indexes)
    except FileMedia.MultipleObjectsReturned:
        return redirect('insecure_file_upload')
