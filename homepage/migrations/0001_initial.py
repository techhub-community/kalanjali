# Generated by Django 2.0.6 on 2018-09-23 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationModel',
            fields=[
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('semester', models.IntegerField()),
                ('event', models.CharField(max_length=20)),
                ('txn_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]
