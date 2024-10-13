 # Generated by Django 5.0.7 on 2024-09-03 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('non_edibile', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Deliveries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('delivery_cost', models.IntegerField()),
                ('resale_value', models.IntegerField()),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliveries.producttype')),
            ],
        ),
    ]
