# Generated by Django 4.1.5 on 2023-04-29 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_rename_sprints_sprint_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='sprint',
        ),
        migrations.DeleteModel(
            name='Sprint',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
