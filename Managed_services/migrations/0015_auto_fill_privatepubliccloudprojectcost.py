from django.db import migrations,models

def create_initial(apps, schema_editor):
    PrivatePublicCloudProjectCost = apps.get_model('Managed_services', 'PrivatePublicCloudProjectCost')
    
    initial_data = [
    {'role_level': 'Linux Engineer - F', 'private_kpi': 300, 'unit': 'Servers', 'support_window': '8x5', 'private_kpi_fte': 0.5, 'public_kpi': 400, 'public_kpi_fte': 0.5},
    {'role_level': 'Linux Engineer - E2', 'private_kpi': 300, 'unit': 'Servers', 'support_window': '8x5', 'private_kpi_fte': 0.35, 'public_kpi': 400, 'public_kpi_fte': 0.35},
    {'role_level': 'Linux Engineer - E3', 'private_kpi': 300, 'unit': 'Servers', 'support_window': '8x5', 'private_kpi_fte': 0.15, 'public_kpi': 400, 'public_kpi_fte': 0.15},
    {'role_level': 'Windows Engineer - F', 'private_kpi': 400, 'unit': 'Servers', 'support_window': '8x5', 'private_kpi_fte': 0.5, 'public_kpi': 450, 'public_kpi_fte': 0.5},
    {'role_level': 'Windows Engineer - E2', 'private_kpi': 400, 'unit': 'Servers', 'support_window': '8x5', 'private_kpi_fte': 0.35, 'public_kpi': 450, 'public_kpi_fte': 0.35},
    {'role_level': 'Windows Engineer - E3', 'private_kpi': 400, 'unit': 'Servers', 'support_window': '8x5', 'private_kpi_fte': 0.15, 'public_kpi': 450, 'public_kpi_fte': 0.15},
    {'role_level': 'Cloud Engineer - OCI Cloud - F', 'private_kpi': 75, 'unit': 'Hosts', 'support_window': '8x5', 'private_kpi_fte': 0.5, 'public_kpi': 100, 'public_kpi_fte': 0.5},
    {'role_level': 'Cloud Engineer - OCI Cloud - E2', 'private_kpi': 75, 'unit': 'Hosts', 'support_window': '8x5', 'private_kpi_fte': 0.35, 'public_kpi': 100, 'public_kpi_fte': 0.35},
    {'role_level': 'Cloud Engineer - OCI Cloud - E3', 'private_kpi': 75, 'unit': 'Hosts', 'support_window': '8x5', 'private_kpi_fte': 0.15, 'public_kpi': 100, 'public_kpi_fte': 0.15},
    {'role_level': 'Storage/Backup - F', 'private_kpi': 1000, 'unit': 'TB', 'support_window': '8x5', 'private_kpi_fte': 0.5, 'public_kpi': 2000, 'public_kpi_fte': 0.5},
    {'role_level': 'Storage/Backup - E2', 'private_kpi': 1000, 'unit': 'TB', 'support_window': '8x5', 'private_kpi_fte': 0.35, 'public_kpi': 2000, 'public_kpi_fte': 0.35},
    {'role_level': 'Storage/Backup - E3', 'private_kpi': 1000, 'unit': 'TB', 'support_window': '8x5', 'private_kpi_fte': 0.15, 'public_kpi': 2000, 'public_kpi_fte': 0.15},
    {'role_level': 'Network Engineer - F', 'private_kpi': 100, 'unit': 'Devices', 'support_window': '8x5', 'private_kpi_fte': 0.5, 'public_kpi': 100, 'public_kpi_fte': 0.5},
    {'role_level': 'Network Engineer - E2', 'private_kpi': 100, 'unit': 'Devices', 'support_window': '8x5', 'private_kpi_fte': 0.25, 'public_kpi': 100, 'public_kpi_fte': 0.35},
    {'role_level': 'Network Engineer - E3', 'private_kpi': 100, 'unit': 'Devices', 'support_window': '8x5', 'private_kpi_fte': 0.25, 'public_kpi': 100, 'public_kpi_fte': 0.15},
    {'role_level': 'Terraform/IaaC Automation Engineer - E2', 'private_kpi': 500, 'unit': 'Devices', 'support_window': '8x5', 'private_kpi_fte': 0.2, 'public_kpi': 500, 'public_kpi_fte': 0.35},
    {'role_level': 'Incident & Problem Manager - E2', 'private_kpi': 1000, 'unit': 'Devices', 'support_window': '8x5', 'private_kpi_fte': 0, 'public_kpi': 1000, 'public_kpi_fte': 0},
    {'role_level': 'Change & Release Manager - E2', 'private_kpi': 2000, 'unit': 'Devices', 'support_window': '8x5', 'private_kpi_fte': 0, 'public_kpi': 2000, 'public_kpi_fte': 0},
    {'role_level': 'RDBMS Admin - E2', 'private_kpi': 50, 'unit': 'DB instances', 'support_window': '8x5', 'private_kpi_fte': 0.7, 'public_kpi': 50, 'public_kpi_fte': 0.7},
    {'role_level': 'RDBMS Admin - E3', 'private_kpi': 50, 'unit': 'DB instances', 'support_window': '8x5', 'private_kpi_fte': 0.3, 'public_kpi': 50, 'public_kpi_fte': 0.3},
    {'role_level': 'Non-RDBMS Admin - E2', 'private_kpi': 50, 'unit': 'DB instances', 'support_window': '8x5', 'private_kpi_fte': 0.7, 'public_kpi': 50, 'public_kpi_fte': 0.7},
    {'role_level': 'Non-RDBMS Admin - E3', 'private_kpi': 50, 'unit': 'DB instances', 'support_window': '8x5', 'private_kpi_fte': 0.3, 'public_kpi': 50, 'public_kpi_fte': 0.3},
    {'role_level': 'AD Admin - E2', 'private_kpi': 5000, 'unit': 'AD Objects', 'support_window': '8x5', 'private_kpi_fte': 0.6, 'public_kpi': 5000, 'public_kpi_fte': 0.6},
    {'role_level': 'AD Admin - E3', 'private_kpi': 5000, 'unit': 'AD Objects', 'support_window': '8x5', 'private_kpi_fte': 0.4, 'public_kpi': 5000, 'public_kpi_fte': 0.4},
    {'role_level': 'Service Desk Lead - B', 'private_kpi': 2000, 'unit': 'Devices', 'support_window': '8x5', 'private_kpi_fte': 0.5, 'public_kpi': 2000, 'public_kpi_fte': 0.5},
    {'role_level': 'Monitoring/Service Desk Engineer - F', 'private_kpi': 1000, 'unit': 'Devices/Services', 'support_window': '24x7', 'private_kpi_fte': 1, 'public_kpi': 1000, 'public_kpi_fte': 1},
    {'role_level': 'Team Lead - E3', 'private_kpi': 0, 'unit': 'Customers', 'support_window': '24x7', 'private_kpi_fte': 0.2, 'public_kpi': 0, 'public_kpi_fte': 0.2},
    {'role_level': 'PMO - E2', 'private_kpi': 0, 'unit': '-', 'support_window': '8x5', 'private_kpi_fte': 0.2, 'public_kpi': 0, 'public_kpi_fte': 0.2},
    {'role_level': 'Delivery Manager - E4', 'private_kpi': 0, 'unit': '-', 'support_window': '8x5', 'private_kpi_fte': 0, 'public_kpi': 0, 'public_kpi_fte': 0},
    {'role_level': 'Delivery Head - E6', 'private_kpi': 0, 'unit': '-', 'support_window': '8x5', 'private_kpi_fte': 0, 'public_kpi': 0, 'public_kpi_fte': 0},
    {'role_level': 'Architect - E4', 'private_kpi': 0, 'unit': '-', 'support_window': '8x5', 'private_kpi_fte': 0, 'public_kpi': 0, 'public_kpi_fte': 0},
    {'role_level': 'DR Manager - E2', 'private_kpi': 0, 'unit': '-', 'support_window': '8x5', 'private_kpi_fte': 0, 'public_kpi': 0, 'public_kpi_fte': 0},
]


    for data in initial_data:
        PrivatePublicCloudProjectCost.objects.create(**data)

class Migration(migrations.Migration):

    dependencies = [
        ('Managed_services', '0014_alter_privatepubliccloudprojectcost_support_window'),
    ]

    operations = [        
        migrations.RunPython(create_initial),  # Insert initial data
    ]
