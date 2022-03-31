# Generated by Django 3.2.12 on 2022-03-31 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20220331_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grade',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('89cfcab7-a054-41bd-9faf-ec247b7ee6cc'), editable=False, primary_key=True, serialize=False, verbose_name='Уникальное поле'),
        ),
        migrations.AlterField(
            model_name='post',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('89cfcab7-a054-41bd-9faf-ec247b7ee6cc'), editable=False, primary_key=True, serialize=False, verbose_name='Уникальное поле'),
        ),
    ]
