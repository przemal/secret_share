from django.forms import CharField
from django.forms import Form
from django.forms import ModelForm
from django.forms.widgets import PasswordInput

from secret_share.user_shares.models import UserShare


class AddUserShareForm(ModelForm):
    class Meta:
        model = UserShare
        fields = ['file', 'url']


class GetUserShareForm(Form):
    secret = CharField(widget=PasswordInput(), max_length=128)
