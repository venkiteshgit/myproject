# Generated by Django 3.1.2 on 2020-10-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_auto_20201019_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insured',
            name='phone_number',
            field=models.CharField(default=-999999900, max_length=15),
        ),
        migrations.AlterField(
            model_name='insured',
            name='ssn',
            field=models.CharField(default=-9099, max_length=15),
        ),
        migrations.AlterField(
            model_name='insured',
            name='zip_code',
            field=models.CharField(default=999999, max_length=30),
        ),
    ]