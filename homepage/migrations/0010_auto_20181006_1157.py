# Generated by Django 2.0.6 on 2018-10-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20180926_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationmodel',
            name='event',
            field=models.CharField(max_length=100),
        ),
    ]
