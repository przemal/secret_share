# Generated by Django 2.2.4 on 2019-08-02 12:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import secret_share.user_shares.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret', models.CharField(default=secret_share.user_shares.models.random_secret, max_length=128)),
                ('access_count', models.IntegerField(default=0, editable=False)),
                ('added', models.DateTimeField(default=datetime.datetime.utcnow, editable=False)),
                ('expires', models.DateTimeField(default=secret_share.user_shares.models.next_day)),
                ('file', models.FileField(blank=True, max_length=200, upload_to='')),
                ('url', models.URLField(blank=True, default=None, max_length=250, null=True)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_shares',
            },
        ),
    ]
