# Generated by Django 4.1.7 on 2023-03-18 20:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_data_branchcount_alter_predictions_branchcount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictions',
            name='unique_Opnd',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.8), django.core.validators.MaxValueValidator(7.9)]),
        ),
    ]
