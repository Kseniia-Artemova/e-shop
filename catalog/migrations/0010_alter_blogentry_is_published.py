# Generated by Django 4.2.4 on 2023-08-16 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_blogentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
    ]
