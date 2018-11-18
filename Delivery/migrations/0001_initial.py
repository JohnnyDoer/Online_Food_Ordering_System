# Generated by Django 2.1.2 on 2018-11-17 17:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('Delivery_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Delivery_Fname', models.CharField(max_length=250)),
                ('Delivery_Lname', models.CharField(max_length=250)),
                ('Delivery_Num', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('Delivery_Area', models.CharField(max_length=250)),
                ('Delivery_Pin', models.CharField(default=0, max_length=6)),
                ('Delivery_City', models.CharField(max_length=250)),
                ('Delivery_State', models.CharField(max_length=250)),
            ],
        ),
    ]