# Generated by Django 2.1.2 on 2018-12-30 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0029_auto_20181230_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='title',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
