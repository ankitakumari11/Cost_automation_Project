# Generated by Django 5.1.1 on 2024-09-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScopingForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('project_name', models.CharField(max_length=255)),
                ('project_status', models.CharField(max_length=10)),
                ('margin', models.DecimalField(decimal_places=2, max_digits=5)),
                ('penalty_risk', models.DecimalField(decimal_places=2, max_digits=5)),
                ('windows_vm', models.PositiveIntegerField()),
                ('linux_vm', models.PositiveIntegerField()),
                ('rdbm_db', models.PositiveIntegerField()),
                ('nosql_db', models.PositiveIntegerField()),
                ('network_devices', models.PositiveIntegerField()),
                ('storage_capacity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('on_call', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('support_window', models.CharField(choices=[('8x5', '8x5'), ('24x7', '24x7'), ('16x5', '16x5')], max_length=10)),
                ('yoy_increment', models.DecimalField(decimal_places=2, max_digits=5)),
                ('active_directory_count', models.PositiveIntegerField()),
                ('contract_duration', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('dc_type', models.CharField(choices=[('Private Cloud', 'Private Cloud'), ('Public Cloud', 'Public Cloud')], max_length=20)),
                ('private_cloud_hosts', models.PositiveIntegerField()),
                ('converged_platform', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('dr_in_scope', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('servers_for_dr', models.PositiveIntegerField()),
                ('dr_drills', models.PositiveIntegerField()),
                ('complexity', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10)),
                ('monitoring', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('patching', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('itsm_services', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('ipc_management', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('travel', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('governance_support', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
            ],
        ),
    ]
