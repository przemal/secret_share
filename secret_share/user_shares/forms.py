from django.forms import ModelForm

from secret_share.user_shares.models import UserShare


class AddUserShareForm(ModelForm):
    class Meta:
        model = UserShare
        fields = ['file', 'url']
