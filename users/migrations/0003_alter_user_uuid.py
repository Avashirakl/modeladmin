# Generated by Django 3.2.12 on 2022-03-31 17:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0b5132d5-7110-47a7-8482-f205bdcd5d24'), editable=False, primary_key=True, serialize=False, verbose_name='Уникальное поле'),
        ),
    ]
