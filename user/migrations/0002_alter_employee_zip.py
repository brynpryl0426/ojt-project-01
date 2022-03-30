# Generated by Django 3.2.4 on 2022-03-30 07:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='zip',
            field=models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator('^([\\s\\d]+)$', 'Only numbers are allowed.')], verbose_name='ZIP'),
        ),
    ]
