# Generated by Django 3.2.5 on 2021-08-01 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0007_auto_20210801_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quoteitem',
            name='price',
        ),
    ]
