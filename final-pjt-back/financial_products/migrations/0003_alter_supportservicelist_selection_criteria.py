# Generated by Django 4.2.16 on 2024-11-22 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_products', '0002_supportservicelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportservicelist',
            name='selection_criteria',
            field=models.TextField(null=True),
        ),
    ]
