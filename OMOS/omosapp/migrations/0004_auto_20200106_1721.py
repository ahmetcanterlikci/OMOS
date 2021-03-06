# Generated by Django 2.2.7 on 2020-01-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omosapp', '0003_myprofilecontent_faicon'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemuser',
            name='tags',
            field=models.ManyToManyField(blank=True, to='omosapp.ClientTag'),
        ),
        migrations.AlterUniqueTogether(
            name='clienttag',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='clienttag',
            name='user',
        ),
    ]
