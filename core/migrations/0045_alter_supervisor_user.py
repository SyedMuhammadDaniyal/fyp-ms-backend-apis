# Generated by Django 4.1.5 on 2023-04-26 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_alter_user_options_alter_user_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
