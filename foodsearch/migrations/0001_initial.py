# Generated by Django 3.0.5 on 2020-04-21 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodDescription',
            fields=[
                ('fdc_id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('data_type', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('food_category_id', models.FloatField(blank=True, null=True)),
                ('publication_date', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'food_description',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FoodNutrient',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('fdc_id', models.BigIntegerField(blank=True, null=True)),
                ('nutrient_id', models.BigIntegerField(blank=True, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('data_points', models.FloatField(blank=True, null=True)),
                ('derivation_id', models.FloatField(blank=True, null=True)),
                ('min', models.FloatField(blank=True, null=True)),
                ('max', models.FloatField(blank=True, null=True)),
                ('median', models.FloatField(blank=True, null=True)),
                ('footnote', models.TextField(blank=True, null=True)),
                ('min_year_acquired', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'food_nutrient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FoodPortion',
            fields=[
                ('fdc_id', models.BigIntegerField(blank=True, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('seq_num', models.FloatField(blank=True, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('measure_unit_id', models.BigIntegerField(blank=True, null=True)),
                ('portion_description', models.TextField(blank=True, null=True)),
                ('modifier', models.TextField(blank=True, null=True)),
                ('gram_weight', models.FloatField(blank=True, null=True)),
                ('data_points', models.FloatField(blank=True, null=True)),
                ('footnote', models.FloatField(blank=True, null=True)),
                ('min_year_acquired', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'food_portion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MeasuringUnit',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'measuring_unit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('unit_name', models.TextField(blank=True, null=True)),
                ('nutrient_nbr', models.FloatField(blank=True, null=True)),
                ('rank', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'nutrient',
                'managed': False,
            },
        ),
    ]
