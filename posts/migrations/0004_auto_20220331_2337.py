# Generated by Django 3.2.12 on 2022-03-31 20:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220331_2319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post'},
        ),
        migrations.AlterField(
            model_name='grade',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('50d22450-4ef3-46d9-ba42-4ab5ccfc4e9f'), editable=False, primary_key=True, serialize=False, verbose_name='Уникальное поле'),
        ),
        migrations.AlterField(
            model_name='post',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('50d22450-4ef3-46d9-ba42-4ab5ccfc4e9f'), editable=False, primary_key=True, serialize=False, verbose_name='Уникальное поле'),
        ),
    ]
