# Generated by Django 2.2.1 on 2019-08-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_match_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='fantacyapp',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('INACTIVE', 'inactive')], default='INACTIVE', max_length=10),
        ),
    ]