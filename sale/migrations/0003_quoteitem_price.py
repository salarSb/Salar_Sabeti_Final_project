# Generated by Django 3.2.5 on 2021-07-31 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_remove_quoteitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='quoteitem',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
