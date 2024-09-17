# Generated by Django 3.2.25 on 2024-09-17 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0210_alter_badgerequest_cert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badgerequest',
            name='badge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='badge_requests', to='judge.badge', verbose_name='badge'),
        ),
    ]
