# Generated by Django 3.2.12 on 2022-03-31 20:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('9ac35932-4bd9-4c18-8e66-83c179eb9ada'), editable=False, primary_key=True, serialize=False, verbose_name='Уникальное поле'),
        ),
    ]
