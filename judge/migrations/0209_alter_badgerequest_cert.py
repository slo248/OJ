# Generated by Django 3.2.25 on 2024-09-17 14:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0208_auto_20240917_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badgerequest',
            name='cert',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions={'pdf'})]),
        ),
    ]
