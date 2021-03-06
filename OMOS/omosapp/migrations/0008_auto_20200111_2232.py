# Generated by Django 2.2.7 on 2020-01-11 22:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('omosapp', '0007_auto_20200111_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='itemName',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='itemPrice',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='item1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='item2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='item3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='item4',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='item5',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='item6',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='item7',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='item8',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='price1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='price2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='price3',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='price4',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='price5',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='price6',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='price7',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clientcategory',
            name='price8',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='chart',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='clientitem',
            unique_together={('user', 'category')},
        ),
        migrations.RemoveField(
            model_name='chart',
            name='clientItem',
        ),
        migrations.RemoveField(
            model_name='clientitem',
            name='name',
        ),
        migrations.RemoveField(
            model_name='clientitem',
            name='price',
        ),
    ]
