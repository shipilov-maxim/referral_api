# Generated by Django 3.2.25 on 2024-10-21 14:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('referrals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referralcode',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 28, 14, 3, 44, 599115, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='referralcode',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
