# Generated by Django 5.1.1 on 2024-11-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcg_api', '0003_api_cards_rarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='api_cards',
            name='trendPrice',
            field=models.FloatField(default=0.0, max_length=255),
        ),
    ]
