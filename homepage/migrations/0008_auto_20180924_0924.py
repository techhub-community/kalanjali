# Generated by Django 2.0.6 on 2018-09-24 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_remove_registrationmodel_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationmodel',
            name='year',
            field=models.IntegerField(),
        ),
    ]
