import random
import string
from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import FileField
from django.db.models import ForeignKey
from django.db.models import IntegerField
from django.db.models import Model
from django.db.models import URLField


def next_day() -> datetime:
    return datetime.utcnow() + timedelta(days=1)


def random_secret() -> str:
    """Generate random 32 characters long alphanumeric string."""
    return ''.join(random.choice(
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits) for _ in range(32))


class UserShare(Model):
    """
    File or URL shares, secured by a secret.
    Each share has an expiration timestamp after which it should not be accessible publicly.
    """
    class Meta:
        db_table = 'user_shares'

    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, editable=False)
    secret = CharField(default=random_secret, max_length=128)  # TODO hash it
    access_count = IntegerField(default=0, editable=False)
    added = DateTimeField(default=datetime.utcnow, editable=False)
    expires = DateTimeField(default=next_day)
    file = FileField(blank=True, max_length=200)
    url = URLField(default=None, blank=True, null=True, max_length=250)  # can be much longer...

    def clean(self):
        if not self.file and self.url is None:
            raise ValidationError('Either file or URL is required')
        elif self.file and self.url:
            raise ValidationError('Only file or URL can be given at the same time')
