# Generated by Django 2.2.7 on 2020-01-12 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omosapp', '0018_order_ordernumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='clientAddress',
            field=models.TextField(null=True),
        ),
    ]
