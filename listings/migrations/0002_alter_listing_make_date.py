# Generated by Django 4.2.4 on 2023-08-16 16:05

from django.db import migrations, models
from django.utils import timezone
import django


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='make_date',
            field=models.DateField(
                blank=True, default=django.utils.timezone.now),
        ),
    ]
