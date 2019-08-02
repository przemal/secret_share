from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import DetailView

from secret_share.user_shares.forms import AddUserShareForm
from secret_share.user_shares.models import UserShare


class AddUserShareView(CreateView):
    form_class = AddUserShareForm
    template_name = 'user_shares/add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.instance.user = request.user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)  # FIXME missing object

    def get_success_url(self):
        return reverse('user_shares:info', kwargs={'pk': self.object.pk})


class UserShareInfoDetailView(DetailView):
    model = UserShare
    template_name = 'user_shares/info.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_object(self, *args, **kwargs):
        object = super().get_object(*args, **kwargs)
        if self.request.user != object.user:
            raise PermissionDenied
        return object
