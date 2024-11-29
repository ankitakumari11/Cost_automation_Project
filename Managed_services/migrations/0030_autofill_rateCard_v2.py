from django.db import migrations, models


def Populate_data(apps, schema_editor):
    RateCard = apps.get_model('Managed_services', 'RateCard')

    # List of data to insert
    initial_data = [
        {'role_hr_band': 'Linux_Engineer_E2', 'level': 'L2', 'experience_years': '3-5 Years', 'responsibility_skills': 'Linux Server Management, L2 level tasks of patching, incident troubleshooting. RHEL/Ubuntu/Centos/SUSE', 'partner_rate': 84000, 'airtel_rate': 84000},
        {'role_hr_band': 'Linux_Engineer_E3', 'level': 'L3', 'experience_years': '5-8 Years', 'responsibility_skills': 'Linux Server Management- L2 skills plus management of HA technologies like Veritas clusters, KVM clusters, OpenShift deployment etc.', 'partner_rate': 134000, 'airtel_rate': 134000},
        {'role_hr_band': 'Linux_Engineer_F', 'level': 'L1', 'experience_years': '1-3 Years', 'responsibility_skills': 'Basic Linux understanding with L1 technical skills to manage daily operations of health checks, Alert troubleshooting etc.', 'partner_rate': 50000, 'airtel_rate': 50000},
        {'role_hr_band': 'Windows_Engineer_E2', 'level': 'L2', 'experience_years': '3-5 Years', 'responsibility_skills': 'Windows Server Management, L2 level tasks of patching, incident troubleshooting. Windows servers, Active Directory basic knowledge', 'partner_rate': 84000, 'airtel_rate': 84000},
        {'role_hr_band': 'Windows_Engineer_E3', 'level': 'L3', 'experience_years': '5-8 Years', 'responsibility_skills': 'Windows Server Management- L2 skills plus management of HA technologies like Windows Clusters, Hyper-V, Active directory advanced skills', 'partner_rate': 134000, 'airtel_rate': 134000},
        {'role_hr_band': 'Windows_Engineer_F', 'level': 'L1', 'experience_years': '1-3 years', 'responsibility_skills': 'Basic Windows understanding with L1 technical skills to manage daily operations of health checks, Alert troubleshooting etc.', 'partner_rate': 50000, 'airtel_rate': 50000},
        {'role_hr_band': 'Cloud_Engineer_OCI_Cloud_E2', 'level': 'L2', 'experience_years': '2-3 Years', 'responsibility_skills': 'Cloud support engineer- Strong experience specifically with Oracle Cloud infrastructure, deployment skills, troubleshooting and operations', 'partner_rate': 84000, 'airtel_rate': 84000},
        {'role_hr_band': 'Cloud_Engineer_OCI_Cloud_E3', 'level': 'L3', 'experience_years': '3-6 Years', 'responsibility_skills': 'Cloud support engineer - L2 skills plus, advanced knowledge on design/architecture, support L3 incidents, OCI certified', 'partner_rate': 134000, 'airtel_rate': 134000},
        {'role_hr_band': 'Cloud_Engineer_OCI_Cloud_F', 'level': 'L1', 'experience_years': '1-2 Years', 'responsibility_skills': '-', 'partner_rate': 90000, 'airtel_rate': 50000},
        {'role_hr_band': 'Storage_Backup_E3', 'level': 'L3', 'experience_years': '5-8 years', 'responsibility_skills': '-', 'partner_rate': 134000, 'airtel_rate': 134000},
        {'role_hr_band': 'Storage_Backup_E2', 'level': 'L2', 'experience_years': '3-5 Years', 'responsibility_skills': 'Storage & Backup Management- Netapp/EMC/HPE/Hitachi, advanced knowledge', 'partner_rate': 84000, 'airtel_rate': 84000},
        {'role_hr_band': 'Storage_Backup_F', 'level': 'L1', 'experience_years': '1-3 years', 'responsibility_skills': 'Basic understanding of storage and should be able to handle daily routine tasks as well as L1 incidents', 'partner_rate': 50000, 'airtel_rate': 50000},
        {'role_hr_band': 'Network_Engineer_E3', 'level': 'L3', 'experience_years': '5-8 years', 'responsibility_skills': '-', 'partner_rate': 134000, 'airtel_rate': 134000},
        {'role_hr_band': 'Network_Engineer_E2', 'level': 'L2', 'experience_years': '3-5 Years', 'responsibility_skills': 'Network Management-Cisco/Juniper/palo Alto device management at L2 level with troubleshooting skills', 'partner_rate': 84000, 'airtel_rate': 84000},
        {'role_hr_band': 'Network_Engineer_F', 'level': 'L1', 'experience_years': '1-3 Years', 'responsibility_skills': 'Basic L1 skilled engineer with good understanding and experience on DC network devices', 'partner_rate': 50000, 'airtel_rate': 50000},
        {'role_hr_band': 'Terraform_IaaC_Automation_Engineer_E2', 'level': 'L2', 'experience_years': '3-5 Years', 'responsibility_skills': 'Tools Integration- Good skills on automation development using Terraform, Ansible or Helm', 'partner_rate': 84000, 'airtel_rate': 84000},
        {'role_hr_band': 'Incident_Problem_Manager_E2', 'level': 'L2', 'experience_years': '2-4 years', 'responsibility_skills': 'Incident Management Skills-Understanding of ITSM processes', 'partner_rate': 84000, 'airtel_rate': 84000},
        {'role_hr_band': 'Change_Release_Manager_E2', 'level': 'L2', 'experience_years': '2-4 Years', 'responsibility_skills': 'Change management Skills-Understanding of ITSM processes', 'partner_rate': 84000, 'airtel_rate': 84000},
        {'role_hr_band': 'RDBMS_Admin_E2', 'level': 'L2', 'experience_years': '3-5 years', 'responsibility_skills': 'Database Management- Any of the database management skills at L2 level', 'partner_rate': 84000, 'airtel_rate': 84000},
        {'role_hr_band': 'RDBMS_Admin_F', 'level': 'L1', 'experience_years': '1-3 years', 'responsibility_skills': 'Basic database management skills with L1 troubleshooting', 'partner_rate': 50000, 'airtel_rate': 50000},
        {'role_hr_band': 'RDBMS_Admin_E3', 'level': 'L3', 'experience_years': '-', 'responsibility_skills': '-', 'partner_rate': 134000, 'airtel_rate': 134000},
        {'role_hr_band': 'Non_RDBMS_Admin_E2', 'level': 'L2', 'experience_years': '3-5 Years', 'responsibility_skills': 'Database Management- Any of the database management skills at L2 level', 'partner_rate': 84000, 'airtel_rate': 84000},
        {'role_hr_band': 'Non_RDBMS_Admin_F', 'level': 'L1', 'experience_years': '1-3 years', 'responsibility_skills': 'Basic database management skills with L1 troubleshooting', 'partner_rate': 50000, 'airtel_rate': 50000},
        {'role_hr_band': 'Non_RDBMS_Admin_E3', 'level': 'L3', 'experience_years': '-', 'responsibility_skills': '-', 'partner_rate': 134000, 'airtel_rate': 134000},
        {'role_hr_band': 'Service_Desk_Lead_B', 'level': 'L2', 'experience_years': '3-5 years', 'responsibility_skills': '24/7 L1 Support Desk lead- experience with monitoring and service desk operations', 'partner_rate': 75000, 'airtel_rate': 75000},
        {'role_hr_band': 'Monitoring_Service_Desk_Engineer_F', 'level': 'L1', 'experience_years': '1-3 years', 'responsibility_skills': '24/7 L1 Support Desk lead- experience with monitoring and service desk operations', 'partner_rate': 50000, 'airtel_rate': 50000},
        {'role_hr_band': 'Team_Lead_E3', 'level': 'L3', 'experience_years': '5-8 years', 'responsibility_skills': 'Team lead for operations, customer handling, escalation Management', 'partner_rate': 134000, 'airtel_rate': 134000},
        {'role_hr_band': 'PMO_E2', 'level': 'L2', 'experience_years': '-', 'responsibility_skills': '-', 'partner_rate': 84000, 'airtel_rate': 84000},
        {'role_hr_band': 'Delivery_Manager_E4', 'level': '-', 'experience_years': '-', 'responsibility_skills': '-', 'partner_rate':  300000, 'airtel_rate': 300000},
        {'role_hr_band': 'Delivery_Head_E6', 'level': '-', 'experience_years': '-', 'responsibility_skills': '-', 'partner_rate': 500000, 'airtel_rate': 500000},
        {'role_hr_band': 'Architect_E4', 'level': '-', 'experience_years': '-', 'responsibility_skills': '-', 'partner_rate': 180000, 'airtel_rate': 180000},
        {'role_hr_band': 'DR_Manager_E2', 'level': 'L2', 'experience_years': '-', 'responsibility_skills': '-', 'partner_rate': 84000, 'airtel_rate': 84000},
        {'role_hr_band': 'Cloud_Security_E3', 'level': 'L3', 'experience_years': '-', 'responsibility_skills': '-', 'partner_rate': 0, 'airtel_rate': 0},
        {'role_hr_band': 'AD_Admin_E2', 'level': 'L2', 'experience_years': '-', 'responsibility_skills': '-', 'partner_rate': 94000, 'airtel_rate': 94000},
        {'role_hr_band': 'AD_Admin_E3', 'level': 'L3', 'experience_years': '-', 'responsibility_skills': '-', 'partner_rate': 144000, 'airtel_rate': 144000},
        
    
    ]


    # Inserting the data into RateCard model
    for data in initial_data:
        RateCard.objects.create(**data)


class Migration(migrations.Migration):

    dependencies = [
        ('Managed_services', '0029_autofill_privatepubliccloudcost_v2'),
    ]

    operations = [
        migrations.RunPython(Populate_data),
    ]