# Generated by Django 3.2.6 on 2022-01-01 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATM', '0002_person_cash_delete_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_200', models.IntegerField(default=200)),
                ('money_100', models.IntegerField(default=200)),
                ('money_50', models.IntegerField(default=200)),
                ('money_20', models.IntegerField(default=200)),
                ('money_10', models.IntegerField(default=200)),
            ],
        ),
    ]
