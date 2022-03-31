# Generated by Django 3.2.12 on 2022-03-31 17:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('6ac8bd31-576e-4869-8f05-cf4ba88b0e06'), editable=False, primary_key=True, serialize=False, verbose_name='Уникальное поле'),
        ),
    ]