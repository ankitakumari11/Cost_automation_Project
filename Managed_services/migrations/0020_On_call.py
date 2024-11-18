from django.db import migrations, models
from decimal import Decimal

def create_initial_on_call_data(apps, schema_editor):
    On_Call = apps.get_model('Managed_services', 'On_Call')
    
    # Insert initial data
    initial_data=[
        {"type":"Weekday", "rate":Decimal('500.00')},
        {"type":"Weekend", "rate":Decimal('1000.00')}
    ]

    for data in initial_data:
        On_Call.objects.create(**data)

class Migration(migrations.Migration):
    dependencies = [
        # Add your previous migration as dependency
        ('Managed_services', '0019_rename_tools_tool'),
    ]

    operations = [
        migrations.CreateModel(
            name='On_Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, choices=[('Weekday', 'Weekday'), ('Weekend', 'Weekend')])),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('no_of_days', models.PositiveIntegerField(blank=True, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.RunPython(create_initial_on_call_data),
    ]
