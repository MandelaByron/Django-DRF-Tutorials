# Generated by Django 5.0.6 on 2024-06-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': [models.OrderBy(models.F('market_value'), descending=True, nulls_last=True), models.OrderBy(models.F('caps'), descending=True, nulls_last=True)]},
        ),
    ]
