from django.db import migrations,models

def create_initial_data(apps, schema_editor):
    PrivateCloudProjectCost = apps.get_model('Managed_services', 'PrivateCloudProjectCost')
    
    initial_data = [
        {'role_level': 'Linux Engineer - F', 'kpi': 300, 'unit': 'Servers', 'support_window': '8x5', 'kpi_fte': 0.5},
        {'role_level': 'Linux Engineer - E2', 'kpi': 300, 'unit': 'Servers', 'support_window': '8x5', 'kpi_fte': 0.35},
        {'role_level': 'Linux Engineer - E3', 'kpi': 300, 'unit': 'Servers', 'support_window': '8x5', 'kpi_fte': 0.15},
        {'role_level': 'Windows Engineer - F', 'kpi': 400, 'unit': 'Servers', 'support_window': '8x5', 'kpi_fte': 0.5},
        {'role_level': 'Windows Engineer - E2', 'kpi': 400, 'unit': 'Servers', 'support_window': '8x5', 'kpi_fte': 0.35},
        {'role_level': 'Windows Engineer - E3', 'kpi': 400, 'unit': 'Servers', 'support_window': '8x5', 'kpi_fte': 0.15},
        {'role_level': 'Cloud Engineer - OCI Cloud - F', 'kpi': 75, 'unit': 'Hosts', 'support_window': '8x5', 'kpi_fte': 0.5},
        {'role_level': 'Cloud Engineer - OCI Cloud - E2', 'kpi': 75, 'unit': 'Hosts', 'support_window': '8x5', 'kpi_fte': 0.35},
        {'role_level': 'Cloud Engineer - OCI Cloud - E3', 'kpi': 75, 'unit': 'Hosts', 'support_window': '8x5', 'kpi_fte': 0.15},
        {'role_level': 'Storage/Backup - F', 'kpi': 1000, 'unit': 'TB', 'support_window': '8x5', 'kpi_fte': 0.5},
        {'role_level': 'Storage/Backup - E2', 'kpi': 1000, 'unit': 'TB', 'support_window': '8x5', 'kpi_fte': 0.35},
        {'role_level': 'Storage/Backup - E3', 'kpi': 1000, 'unit': 'TB', 'support_window': '8x5', 'kpi_fte': 0.15},
        {'role_level': 'Network Engineer - F', 'kpi': 100, 'unit': 'Devices', 'support_window': '8x5', 'kpi_fte': 0.5},
        {'role_level': 'Network Engineer - E2', 'kpi': 100, 'unit': 'Devices', 'support_window': '8x5', 'kpi_fte': 0.25},
        {'role_level': 'Network Engineer - E3', 'kpi': 100, 'unit': 'Devices', 'support_window': '8x5', 'kpi_fte': 0.25},
        {'role_level': 'Terraform/IaaC Automation Engineer - E2', 'kpi': 500, 'unit': 'Devices', 'support_window': '8x5', 'kpi_fte': 0.2},
        {'role_level': 'Incident & Problem Manager - E2', 'kpi': 1000, 'unit': 'Devices', 'support_window': '8x5', 'kpi_fte': 0},
        {'role_level': 'Change & Release Manager - E2', 'kpi': 2000, 'unit': 'Devices', 'support_window': '8x5', 'kpi_fte': 0},
        {'role_level': 'RDBMS Admin - E2', 'kpi': 50, 'unit': 'DB instances', 'support_window': '8x5', 'kpi_fte': 0.7},
        {'role_level': 'RDBMS Admin - E3', 'kpi': 50, 'unit': 'DB instances', 'support_window': '8x5', 'kpi_fte': 0.3},
        {'role_level': 'Non-RDBMS Admin - E2', 'kpi': 50, 'unit': 'DB instances', 'support_window': '8x5', 'kpi_fte': 0.7},
        {'role_level': 'Non-RDBMS Admin - E3', 'kpi': 50, 'unit': 'DB instances', 'support_window': '8x5', 'kpi_fte': 0.3},
        {'role_level': 'AD Admin - E2', 'kpi': 5000, 'unit': 'AD Objects', 'support_window': '8x5', 'kpi_fte': 0.6},
        {'role_level': 'AD Admin - E3', 'kpi': 5000, 'unit': 'AD Objects', 'support_window': '8x5', 'kpi_fte': 0.4},
        {'role_level': 'Service Desk Lead - B', 'kpi': 2000, 'unit': 'Devices', 'support_window': '8x5', 'kpi_fte': 0.5},
        {'role_level': 'Monitoring/Service Desk Engineer - F', 'kpi': 1000, 'unit': 'Devices/Services', 'support_window': '24x7', 'kpi_fte': 1},
        {'role_level': 'Team Lead - E3', 'kpi': 0, 'unit': 'Customers', 'support_window': '24x7', 'kpi_fte': 0.2},
        {'role_level': 'PMO - E2', 'kpi': 0, 'unit': 'Customers', 'support_window': '8x5', 'kpi_fte': 0.2},
        {'role_level': 'Delivery Manager - E4', 'kpi': 0, 'unit': 'Customers', 'support_window': '8x5', 'kpi_fte': 0},
        {'role_level': 'Delivery Head - E6', 'kpi': 0, 'unit': 'Customers', 'support_window': '8x5', 'kpi_fte': 0},
        {'role_level': 'Architect - E4', 'kpi': 0, 'unit': 'Customers', 'support_window': '8x5', 'kpi_fte': 0},
        {'role_level': 'DR Manager - E2', 'kpi': 0, 'unit': 'Customers', 'support_window': '8x5', 'kpi_fte': 0},
    ]

    for data in initial_data:
        PrivateCloudProjectCost.objects.create(**data)

class Migration(migrations.Migration):

    dependencies = [
        ('Managed_services', '0004_travel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateCloudProjectCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('role_level', models.CharField(max_length=100)),
                ('kpi', models.IntegerField()),
                ('unit', models.CharField(max_length=50)),
                ('support_window', models.CharField(max_length=10)),
                ('kpi_fte', models.FloatField()),
                ('project_volume', models.IntegerField(blank=True, null=True)),
                ('project_fte', models.FloatField(blank=True, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_monthly', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('complex', models.BooleanField(default=False)),
            ],
        ),
        migrations.RunPython(create_initial_data),  # Insert initial data
    ]
