# Generated by Django 5.1.1 on 2024-11-13 15:49

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Managed_services', '0023_alter_tool_quantity_alter_tool_rate_per_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scopingform',
            name='description',
            field=models.TextField(blank=True, default='No description provided', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='scopingform',
            name='location',
            field=models.CharField(default='Not specified', max_length=255),
        ),
        migrations.AddField(
            model_name='scopingform',
            name='received_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='scopingform',
            name='submission_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='scopingform',
            name='tcv',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='TCV (in Crore)'),
        ),
        migrations.AlterField(
            model_name='scopingform',
            name='project_status',
            field=models.CharField(choices=[('Active', 'Active'), ('Cancelled', 'Cancelled'), ('Closed', 'Closed'), ('Dropped', 'Dropped'), ('Hold', 'Hold'), ('Lost', 'Lost'), ('Passive', 'Passive'), ('Submitted', 'Submitted'), ('Won', 'Won')], max_length=10),
        ),
    ]
