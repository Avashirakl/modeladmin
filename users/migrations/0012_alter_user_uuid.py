# Generated by Django 3.2.12 on 2022-03-31 20:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('89cfcab7-a054-41bd-9faf-ec247b7ee6cc'), editable=False, primary_key=True, serialize=False, verbose_name='Уникальное поле'),
        ),
    ]