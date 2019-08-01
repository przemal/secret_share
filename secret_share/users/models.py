from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    class Meta:
        db_table = 'users'

    last_user_agent = CharField(blank=True, max_length=250)
