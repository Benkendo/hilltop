# Generated by Django 5.0.4 on 2024-06-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_companylogo'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='year_of_manufacture',
            field=models.PositiveIntegerField(default=2000),
        ),
    ]
