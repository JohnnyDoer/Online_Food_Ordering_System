# Generated by Django 2.1.3 on 2018-12-11 13:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('Food_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Food_Name', models.CharField(max_length=250)),
                ('Food_Price', models.IntegerField()),
                ('Food_Pic', models.ImageField(default='media/default_food.jpg', upload_to='media')),
                ('Food_Discount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('FoodCategory_ID', models.AutoField(primary_key=True, serialize=False)),
                ('FoodCategory_Name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('Restaurant_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Restaurant_Name', models.CharField(max_length=250)),
                ('Restaurant_Street', models.CharField(max_length=250)),
                ('Restaurant_Pin', models.CharField(default=132658, max_length=6)),
                ('Restaurant_Phone_Number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('Restaurant_Logo', models.ImageField(default='media/default_res.jpg', upload_to='media')),
                ('Restaurant_Ratings_Count', models.IntegerField(default=0)),
                ('Restaurant_Rating', models.IntegerField(default=0, verbose_name=django.core.validators.MaxValueValidator(10))),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Restaurants.Area')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Restaurants.City')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='Food_Category_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurants.FoodCategory'),
        ),
        migrations.AddField(
            model_name='food',
            name='Food_Res_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurants.Restaurant'),
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurants.City'),
        ),
    ]
