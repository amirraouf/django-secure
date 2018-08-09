from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView, DetailView

from insecure_app.forms import UploadForm
from insecure_app.models import FileMedia


class InSecureUserCreateView(LoginRequiredMixin, CreateView):
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


class InSecureUserRetrieveView(LoginRequiredMixin, TemplateView):
    """
    Retrieve users to show that passwords not hashed and are plain
    """
    extra_context = {
        'users': get_user_model().objects.all()
    }
    template_name = 'common/users.html'


class InSecureFileUploadView(LoginRequiredMixin, CreateView):
    """
    Simple view for showing insecure file upload to apply:
    OTG-BUSLOGIC-008: Unexpected uploaded file types
    OTG-BUSLOGIC-009: Test Upload of Malicious Files
    """
    template_name = 'common/file_upload.html'
    form_class = UploadForm


class InSecureFileDownloadView(LoginRequiredMixin, DetailView):
    slug_field = 'pk'
    model = FileMedia
    template_name = 'common/filemedia_detail.html'



@login_required
def insecure_doc_download(request, pk):
    """
    Function Based View
    Downloads Media file that user had uploaded before.
    I
    :param request: HttpRequest that handles user details.
    :param doc_id: Document's id to be fetched.
    :return: Downloadable excel or 404.
    """
    try:
        document = FileMedia.objects.get(id=pk)

        response = HttpResponse(document.file, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=%s' % document.filename()
        response['X-Accel-Redirect'] = '/media/' + document.upload.name

        return response
    except FileMedia.DoesNotExist:
        raise Http404


