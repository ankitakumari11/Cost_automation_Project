# Generated by Django 5.1.1 on 2024-10-21 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Managed_services', '0007_alter_privatecloudprojectcost_complex_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatecloudprojectcost',
            name='project_fte',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='privatecloudprojectcost',
            name='project_volume',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='privatecloudprojectcost',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='privatecloudprojectcost',
            name='total_monthly',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='scopingform',
            name='margin',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='scopingform',
            name='penalty_risk',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='scopingform',
            name='total_storage_capacity',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='scopingform',
            name='yoy_increment',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
