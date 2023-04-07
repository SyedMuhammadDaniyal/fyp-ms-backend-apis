# Generated by Django 4.1.5 on 2023-03-26 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_project_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=75)),
                ('isactive', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=500)),
                ('createdate', models.DateField()),
                ('createtime', models.TimeField()),
                ('createdby', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.fyppanel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
