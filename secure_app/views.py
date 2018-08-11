from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView
from django.views.static import serve

from secure_app.forms import SecureUploadForm
from insecure_app.models import FileMedia


class SecureUserCreateView(LoginRequiredMixin, CreateView):
    """
    Simple view to create an Auth user using Generic CreateView
    It automatically creates an instance of model defined and use
    form class using the template name

    It will create a user with hash password as User Creation will use
    Users.objects.create_user(**kwargs) --> This hashes the password
    """
    model = get_user_model()
    template_name = 'common/secure_create.html'
    success_url = reverse_lazy('insecure_app.insecure_users')
    form_class = UserCreationForm


class SecureFileUploadView(LoginRequiredMixin, CreateView):
    """
    Simple view for showing insecure file upload to apply:
    OTG-BUSLOGIC-008: Unexpected uploaded file types
    OTG-BUSLOGIC-009: Test Upload of Malicious Files
    """
    template_name = 'common/file_upload.html'
    form_class = SecureUploadForm

    def get_success_url(self):
        return self.object.secure_get_absolute_url()


class SecureFileView(LoginRequiredMixin, DetailView):
    """
    url detecting is solved as the user can't detect the url slug kwargs
    user can detect /view/1/ and /view/2/ but /view/<randomsting> hard to be detected
    """
    slug_url_kwarg = 'ref'
    slug_field = 'ref'
    model = FileMedia
    template_name = 'common/secure_filemedia_detail.html'


@login_required
def secure_doc_download(request, ref):
    """
    Function Based View
    Downloads Media file that user had uploaded before.
    It is insecure as if you saved the file url you can download it and you're not logged in
    :param request: HttpRequest that handles user details.
    :param doc_id: Document's id to be fetched.
    :return: Downloadable excel or 404.
    """
    try:
        document = FileMedia.objects.get(ref=ref)

        response = HttpResponse(document.file, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(document.filename())
        response['X-Accel-Redirect'] = 'secure/media/' + document.upload.name

        return response
    except FileMedia.DoesNotExist:
        raise Http404


@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    """
    Protected Serve view is a protected django static serve
    function for adding more extra security for downloading media
    to solve
    Now if you requested /media/2018/loremipsum.ext it will be downloaded
    however you're not logged in, that's why django static serve view
    is not secured by authenticated users only.
    Try /secure/media/2018/loremipsum.ext
    :param request: request of user
    :param path: path of the document
    :param document_root: media root directory
    :param show_indexes: This is False by default. If it's True, Django will display file listings for directories.
    :return: serve function view
    """
    if request.user.has_perm('insecure_app.view_filemedia'):
        return serve(request, path, document_root, show_indexes)
    else:
        return redirect('insecure_file_upload')
