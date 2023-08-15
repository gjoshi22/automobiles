# Generated by Django 4.2.4 on 2023-08-13 23:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('engine_size', models.IntegerField()),
                ('horse_power', models.IntegerField()),
                ('mileage', models.FloatField()),
                ('weight', models.FloatField()),
                ('torque', models.FloatField()),
                ('category', models.CharField(max_length=15)),
                ('fuel_type', models.CharField(max_length=10)),
                ('make_date', models.PositiveIntegerField()),
                ('photo_main', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateField(blank=True, default=datetime.date(2023, 8, 13))),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='seller.seller')),
            ],
        ),
    ]
