# Generated by Django 3.1.4 on 2021-01-19 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20210108_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='spice_index',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
