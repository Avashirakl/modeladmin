# Generated by Django 3.2.12 on 2022-03-31 22:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('d1b91913-6b42-4e42-a905-bfe52be29d26'), editable=False, primary_key=True, serialize=False, verbose_name='Уникальное поле'),
        ),
    ]
