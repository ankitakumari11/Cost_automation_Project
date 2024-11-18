from django.db import migrations, models
from django.db import migrations

def create_initial_calculation_data(apps, schema_editor):
    CostCalculation = apps.get_model('Managed_services', 'CostCalculation')
    initial_categories = [
        'Resources Cost', 'Tools', 'OnCall', 'Travel', 
        'Overhead', 'Margin', 'Penalty Risk', 'Sum'
    ]
    
    for category in initial_categories:
        CostCalculation.objects.create(cost_category=category)

class Migration(migrations.Migration):

    dependencies = [
        # Define the dependency for this migration
        ('Managed_services', '0020_On_call'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostCalculation',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('cost_category', models.CharField(max_length=50)),
                ('monthly', models.DecimalField(max_digits=12, decimal_places=2, default=0.00)),
                ('y1', models.DecimalField(max_digits=12, decimal_places=2, default=0.00)),
                ('y2', models.DecimalField(max_digits=12, decimal_places=2, default=0.00)),
                ('y3', models.DecimalField(max_digits=12, decimal_places=2, default=0.00)),
                ('y4', models.DecimalField(max_digits=12, decimal_places=2, default=0.00)),
                ('y5', models.DecimalField(max_digits=12, decimal_places=2, default=0.00)),
            ],
        ),
        migrations.RunPython(create_initial_calculation_data),
    ]