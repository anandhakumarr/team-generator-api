# Generated by Django 2.2.1 on 2019-09-15 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20190914_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='fantacyapp',
            field=models.ManyToManyField(to='api.FantacyApp'),
        ),
    ]
