# Generated by Django 2.2.1 on 2019-08-24 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_fantacysport_fantacy_rules'),
    ]

    operations = [
        migrations.AddField(
            model_name='fantacysport',
            name='skills',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
