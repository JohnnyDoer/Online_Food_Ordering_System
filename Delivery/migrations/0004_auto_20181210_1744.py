# Generated by Django 2.1.3 on 2018-12-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delivery', '0003_auto_20181202_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='Delivery_Pic',
            field=models.ImageField(default='media/default_profile.jpg', upload_to='media'),
        ),
    ]
