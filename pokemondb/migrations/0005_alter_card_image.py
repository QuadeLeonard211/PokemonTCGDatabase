# Generated by Django 5.1.1 on 2024-10-31 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemondb', '0004_card_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.CharField(default='images/1-Venusaur-ex-Stellar-Crown.png', max_length=256),
        ),
    ]
