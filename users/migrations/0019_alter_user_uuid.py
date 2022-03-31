# Generated by Django 3.2.12 on 2022-03-31 22:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('98734087-f92e-42b9-bcd6-bffcce1a3dc4'), editable=False, primary_key=True, serialize=False, verbose_name='Уникальное поле'),
        ),
    ]