# Generated by Django 5.1.1 on 2024-12-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Managed_services', '0036_alter_scopingform_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='costsummary',
            name='SA_name',
            field=models.CharField(default='Not Assigned', max_length=255),
        ),
        migrations.AddField(
            model_name='costsummary',
            name='product_name',
            field=models.CharField(default='No product_name provided', max_length=50),
        ),
        migrations.AddField(
            model_name='projectresourceutilisation',
            name='SA_name',
            field=models.CharField(default='Not Assigned', max_length=255),
        ),
        migrations.AddField(
            model_name='projectresourceutilisation',
            name='product_name',
            field=models.CharField(default='No product_name provided', max_length=50),
        ),
        migrations.AddField(
            model_name='yearlycostsummary',
            name='SA_name',
            field=models.CharField(default='Not Assigned', max_length=255),
        ),
        migrations.AddField(
            model_name='yearlycostsummary',
            name='product_name',
            field=models.CharField(default='No product_name provided', max_length=50),
        ),
    ]
