# Generated by Django 3.2.12 on 2022-03-31 20:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('50d22450-4ef3-46d9-ba42-4ab5ccfc4e9f'), editable=False, primary_key=True, serialize=False, verbose_name='Уникальное поле'),
        ),
    ]