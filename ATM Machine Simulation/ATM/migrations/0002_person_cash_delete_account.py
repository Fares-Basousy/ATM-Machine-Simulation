# Generated by Django 4.0 on 2021-12-31 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='cash',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='account',
        ),
    ]