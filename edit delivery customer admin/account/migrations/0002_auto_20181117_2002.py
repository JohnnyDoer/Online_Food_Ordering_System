# Generated by Django 2.1.3 on 2018-11-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='area',
            field=models.CharField(default='abc', max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='state',
            field=models.CharField(default='abc', max_length=255),
        ),
    ]
