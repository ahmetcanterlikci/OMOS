# Generated by Django 2.2.7 on 2020-01-12 13:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('omosapp', '0012_chart_itemcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
