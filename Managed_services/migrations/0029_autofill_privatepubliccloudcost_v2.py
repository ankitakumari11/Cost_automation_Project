from django.db import migrations,models

def create_data(apps, schema_editor):
    PrivatePublicCloudProjectCost = apps.get_model('Managed_services', 'PrivatePublicCloudProjectCost')
    
    initial_data = [
    {'role_level': 'Linux_Engineer_F', 'private_kpi': 300, 'unit': 'Servers', 'support_window': '8x5', 'private_kpi_fte': 0.5, 'public_kpi': 400, 'public_kpi_fte': 0.5},
    {'role_level': 'Linux_Engineer_E2', 'private_kpi': 300, 'unit': 'Servers', 'support_window': '8x5', 'private_kpi_fte': 0.35, 'public_kpi': 400, 'public_kpi_fte': 0.35},
    {'role_level': 'Linux_Engineer_E3', 'private_kpi': 300, 'unit': 'Servers', 'support_window': '8x5', 'private_kpi_fte': 0.15, 'public_kpi': 400, 'public_kpi_fte': 0.15},
    {'role_level': 'Windows_Engineer_F', 'private_kpi': 400, 'unit': 'Servers', 'support_window': '8x5', 'private_kpi_fte': 0.5, 'public_kpi': 450, 'public_kpi_fte': 0.5},
    {'role_level': 'Windows_Engineer_E2', 'private_kpi': 400, 'unit': 'Servers', 'support_window': '8x5', 'private_kpi_fte': 0.35, 'public_kpi': 450, 'public_kpi_fte': 0.35},
    {'role_level': 'Windows_Engineer_E3', 'private_kpi': 400, 'unit': 'Servers', 'support_window': '8x5', 'private_kpi_fte': 0.15, 'public_kpi': 450, 'public_kpi_fte': 0.15},
    {'role_level': 'Cloud_Engineer_OCI_Cloud_F', 'private_kpi': 75, 'unit': 'Hosts', 'support_window': '8x5', 'private_kpi_fte': 0.5, 'public_kpi': 100, 'public_kpi_fte': 0.5},
    {'role_level': 'Cloud_Engineer_OCI_Cloud_E2', 'private_kpi': 75, 'unit': 'Hosts', 'support_window': '8x5', 'private_kpi_fte': 0.35, 'public_kpi': 100, 'public_kpi_fte': 0.35},
    {'role_level': 'Cloud_Engineer_OCI_Cloud_E3', 'private_kpi': 75, 'unit': 'Hosts', 'support_window': '8x5', 'private_kpi_fte': 0.15, 'public_kpi': 100, 'public_kpi_fte': 0.15},
    {'role_level': 'Storage_Backup_F', 'private_kpi': 1000, 'unit': 'TB', 'support_window': '8x5', 'private_kpi_fte': 0.5, 'public_kpi': 2000, 'public_kpi_fte': 0.5},
    {'role_level': 'Storage_Backup_E2', 'private_kpi': 1000, 'unit': 'TB', 'support_window': '8x5', 'private_kpi_fte': 0.35, 'public_kpi': 2000, 'public_kpi_fte': 0.35},
    {'role_level': 'Storage_Backup_E3', 'private_kpi': 1000, 'unit': 'TB', 'support_window': '8x5', 'private_kpi_fte': 0.15, 'public_kpi': 2000, 'public_kpi_fte': 0.15},
    {'role_level': 'Network_Engineer_F', 'private_kpi': 100, 'unit': 'Devices', 'support_window': '8x5', 'private_kpi_fte': 0.5, 'public_kpi': 100, 'public_kpi_fte': 0.5},
    {'role_level': 'Network_Engineer_E2', 'private_kpi': 100, 'unit': 'Devices', 'support_window': '8x5', 'private_kpi_fte': 0.25, 'public_kpi': 100, 'public_kpi_fte': 0.35},
    {'role_level': 'Network_Engineer_E3', 'private_kpi': 100, 'unit': 'Devices', 'support_window': '8x5', 'private_kpi_fte': 0.25, 'public_kpi': 100, 'public_kpi_fte': 0.15},
    {'role_level': 'Terraform_IaaC_Automation_Engineer_E2', 'private_kpi': 500, 'unit': 'Devices', 'support_window': '8x5', 'private_kpi_fte': 0.2, 'public_kpi': 500, 'public_kpi_fte': 0.35},
    {'role_level': 'Incident_Problem_Manager_E2', 'private_kpi': 1000, 'unit': 'Devices', 'support_window': '8x5', 'private_kpi_fte': 0, 'public_kpi': 1000, 'public_kpi_fte': 0},
    {'role_level': 'Change_Release_Manager_E2', 'private_kpi': 2000, 'unit': 'Devices', 'support_window': '8x5', 'private_kpi_fte': 0, 'public_kpi': 2000, 'public_kpi_fte': 0},
    {'role_level': 'RDBMS_Admin_E2', 'private_kpi': 50, 'unit': 'DB instances', 'support_window': '8x5', 'private_kpi_fte': 0.7, 'public_kpi': 50, 'public_kpi_fte': 0.7},
    {'role_level': 'RDBMS_Admin_E3', 'private_kpi': 50, 'unit': 'DB instances', 'support_window': '8x5', 'private_kpi_fte': 0.3, 'public_kpi': 50, 'public_kpi_fte': 0.3},
    {'role_level': 'Non_RDBMS_Admin_E2', 'private_kpi': 50, 'unit': 'DB instances', 'support_window': '8x5', 'private_kpi_fte': 0.7, 'public_kpi': 50, 'public_kpi_fte': 0.7},
    {'role_level': 'Non_RDBMS_Admin_E3', 'private_kpi': 50, 'unit': 'DB instances', 'support_window': '8x5', 'private_kpi_fte': 0.3, 'public_kpi': 50, 'public_kpi_fte': 0.3},
    {'role_level': 'AD_Admin_E2', 'private_kpi': 5000, 'unit': 'AD Objects', 'support_window': '8x5', 'private_kpi_fte': 0.6, 'public_kpi': 5000, 'public_kpi_fte': 0.6},
    {'role_level': 'AD_Admin_E3', 'private_kpi': 5000, 'unit': 'AD Objects', 'support_window': '8x5', 'private_kpi_fte': 0.4, 'public_kpi': 5000, 'public_kpi_fte': 0.4},
    {'role_level': 'Service_Desk_Lead_B', 'private_kpi': 2000, 'unit': 'Devices', 'support_window': '8x5', 'private_kpi_fte': 0.5, 'public_kpi': 2000, 'public_kpi_fte': 0.5},
    {'role_level': 'Monitoring_Service_Desk_Engineer_F', 'private_kpi': 1000, 'unit': 'Devices/Services', 'support_window': '24x7', 'private_kpi_fte': 1, 'public_kpi': 1000, 'public_kpi_fte': 1},
    {'role_level': 'Team_Lead_E3', 'private_kpi': 0, 'unit': 'Customers', 'support_window': '24x7', 'private_kpi_fte': 0.2, 'public_kpi': 0, 'public_kpi_fte': 0.2},
    {'role_level': 'PMO_E2', 'private_kpi': 0, 'unit': '-', 'support_window': '8x5', 'private_kpi_fte': 0.2, 'public_kpi': 0, 'public_kpi_fte': 0.2},
    {'role_level': 'Delivery_Manager_E4', 'private_kpi': 0, 'unit': '-', 'support_window': '8x5', 'private_kpi_fte': 0, 'public_kpi': 0, 'public_kpi_fte': 0},
    {'role_level': 'Delivery_Head_E6', 'private_kpi': 0, 'unit': '-', 'support_window': '8x5', 'private_kpi_fte': 0, 'public_kpi': 0, 'public_kpi_fte': 0},
    {'role_level': 'Architect_E4', 'private_kpi': 0, 'unit': '-', 'support_window': '8x5', 'private_kpi_fte': 0, 'public_kpi': 0, 'public_kpi_fte': 0},
    {'role_level': 'DR_Manager_E2', 'private_kpi': 0, 'unit': '-', 'support_window': '8x5', 'private_kpi_fte': 0, 'public_kpi': 0, 'public_kpi_fte': 0},
]


    for data in initial_data:
        PrivatePublicCloudProjectCost.objects.create(**data)

class Migration(migrations.Migration):

    dependencies = [
        ('Managed_services', '0028_rename_cloud_engineer_vmware_redhat_e2_projectresourceutilisation_cloud_engineer_oci_cloud_e2_and_mo'),
    ]

    operations = [        
        migrations.RunPython(create_data),  # Insert initial data
    ]
