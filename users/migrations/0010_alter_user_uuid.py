# Generated by Django 3.2.12 on 2022-03-31 20:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('f04a68e6-3d6c-4900-9748-05091b2075a3'), editable=False, primary_key=True, serialize=False, verbose_name='Уникальное поле'),
        ),
    ]
