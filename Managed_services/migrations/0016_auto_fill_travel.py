from django.db import migrations,models

def create_initial(apps, schema_editor):
    Travel = apps.get_model('Managed_services', 'Travel')
    
    initial_data = [
    {'type': 'Airfare', 'unit': 'Trips', 'quantity': 1, 'rate': 10000},
    {'type': 'Hotel', 'unit': 'Days', 'quantity': 3, 'rate':7500},
    {'type': 'Expenses', 'unit': 'Days', 'quantity': 3, 'rate': 1200},
    {'type': 'Taxi', 'unit': 'Trips', 'quantity': 8, 'rate': 600},
   
]


    for data in initial_data:
        # Calculate total before saving
        data['total'] = data['quantity'] * data['rate']
        Travel.objects.create(**data)

class Migration(migrations.Migration):

    dependencies = [
        ('Managed_services', '0015_auto_fill_privatepubliccloudprojectcost'),
    ]

    operations = [        
        migrations.RunPython(create_initial),  # Insert initial data
    ]
