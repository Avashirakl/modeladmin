# Generated by Django 3.2.12 on 2022-03-31 21:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('efda956f-380d-4952-a3ca-d3cd03ca7814'), editable=False, primary_key=True, serialize=False, verbose_name='Уникальное поле'),
        ),
    ]
