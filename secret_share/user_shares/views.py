from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import F
from django.http import FileResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from secret_share.user_shares.forms import AddUserShareForm
from secret_share.user_shares.forms import GetUserShareForm
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


class UserShareView(FormMixin, DetailView):
    form_class = GetUserShareForm
    model = UserShare
    template_name = 'user_shares/get.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid() and form.cleaned_data.get('secret') == self.object.secret:
            if self.object.is_expired():
                # TODO return error message
                return self.form_invalid(form)
            self.object.access_count = F('access_count') + 1  # prevent race
            self.object.save()
            if self.object.is_url():
                return redirect(self.object.url)
            else:
                return FileResponse(
                    self.object.file.open(),
                    as_attachment=True,
                    filename=self.object.file.name)
        else:
            return self.form_invalid(form)


class UserShareInfoDetailView(DetailView):
    model = UserShare
    template_name = 'user_shares/info.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['absolute_url'] = self.request.build_absolute_uri(
            reverse('user_shares:get', kwargs={'pk': self.object.pk}))
        return data

    def get_object(self, *args, **kwargs):
        object = super().get_object(*args, **kwargs)
        if self.request.user != object.user:
            raise PermissionDenied
        return object
