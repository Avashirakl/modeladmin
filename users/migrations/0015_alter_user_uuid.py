# Generated by Django 3.2.12 on 2022-03-31 22:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('a6560a08-c2f3-4573-bc1d-b6e2268e1e91'), editable=False, primary_key=True, serialize=False, verbose_name='Уникальное поле'),
        ),
    ]
