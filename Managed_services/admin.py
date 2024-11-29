from django.contrib import admin
from .models import ScopingForm ,RateCard,Travel,PrivatePublicCloudProjectCost, Tool,On_Call , CostCalculation ,CostSummary , YearlyCostSummary ,ProjectResourceUtilisation
import pandas as pd
from django.http import HttpResponse
# Register your models here.

# Common export function for all models
def export_to_excel(modeladmin, request, queryset):
    # If no rows are selected, use all records from the model
    if not queryset:  # if the queryset is empty (no rows selected)
        queryset = modeladmin.model.objects.all()  # fetch all records for the model
    
    # Convert the queryset to a list of dictionaries, excluding the 'id' field
    data = list(queryset.values())
    
    # Remove the 'id' key from each dictionary in the data list
    for record in data:
        record.pop('id', None)

    # Convert the list of dictionaries into a Pandas DataFrame
    df = pd.DataFrame(data)

    # Create an HTTP response with Excel file content
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={modeladmin.model._meta.model_name}_data.xlsx'

    # Save the DataFrame to the response as an Excel file
    df.to_excel(response, index=False)

    return response



# Define a custom admin class to customize how the model is displayed
class ScopingFormAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'project_name','location','received_date','submission_date', 'project_status', 'margin', 'penalty_risk',
        'no_of_windows_vms', 'no_of_linux_vms', 'no_of_rdbms_dbs', 'no_of_nosql_dbs',
        'no_of_network_devices','Total_VMs_Devices', 'total_storage_capacity', 'on_call', 
        'support_window', 'yoy_increment', 'no_of_ad_objects',
        'contract_duration', 'dc_type', 'no_of_private_cloud_hosts',
        'hyper_converged_platform_used', 'dr_in_scope', 'no_of_servers_for_dr', 
        'dr_drills', 'complexity', 'monitoring', 'patching',
        'itsm_services', 'ipc_management_in_scope', 'travel', 'management_governance_support','tcv')
    actions = [export_to_excel]  # Add the export action
    
# Register the model with the custom admin class
admin.site.register(ScopingForm, ScopingFormAdmin)


@admin.register(RateCard)
class RateCardAdmin(admin.ModelAdmin):
    list_display = ('role_hr_band','level', 'experience_years', 'partner_rate', 'airtel_rate','responsibility_skills')
    actions = [export_to_excel]  # Add the export action

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('type', 'unit', 'quantity', 'rate', 'total')
    actions = [export_to_excel]  # Add the export action



# Register the custom admin action
class PrivatePublicCloudProjectCostAdmin(admin.ModelAdmin):
    list_display = ('role_level','private_kpi', 'public_kpi', 'unit', 'support_window', 'private_kpi_fte','public_kpi_fte','project_volume','project_fte','rate','total_monthly','complex') # Customize as needed
    actions = [export_to_excel]  # Add the export action

# Register the model and the admin class
admin.site.register(PrivatePublicCloudProjectCost, PrivatePublicCloudProjectCostAdmin)


# @admin.register(PrivatePublicCloudProjectCost)
# class PrivateCloudProjectCostAdmin(admin.ModelAdmin):
#     list_display = ('role_level','private_kpi', 'public_kpi', 'unit', 'support_window', 'private_kpi_fte','public_kpi_fte','project_volume','project_fte','rate','total_monthly','complex')

@admin.register(ProjectResourceUtilisation)
class ProjectResourceUtilisationAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 
                    'Linux_Engineer_F', 'Linux_Engineer_E2', 'Linux_Engineer_E3', 
                    'Windows_Engineer_F', 'Windows_Engineer_E2', 'Windows_Engineer_E3', 
                    'Cloud_Engineer_OCI_Cloud_F', 'Cloud_Engineer_OCI_Cloud_E2', 'Cloud_Engineer_OCI_Cloud_E3', 
                    'Storage_Backup_F', 'Storage_Backup_E2', 'Storage_Backup_E3', 
                    'Network_Engineer_F', 'Network_Engineer_E2', 'Network_Engineer_E3', 
                    'Terraform_IaaC_Automation_Engineer_E2', 'Incident_Problem_Manager_E2', 
                    'Change_Release_Manager_E2', 'RDBMS_Admin_E2', 'RDBMS_Admin_E3', 
                    'Non_RDBMS_Admin_E2', 'Non_RDBMS_Admin_E3', 'AD_Admin_E2', 'AD_Admin_E3', 
                    'Service_Desk_Lead_B', 'Monitoring_Service_Desk_Engineer_F', 'Team_Lead_E3', 
                    'PMO_E2', 'Delivery_Manager_E4', 'Delivery_Head_E6', 'Architect_E4', 'DR_Manager_E2')
    actions = [export_to_excel]
    
@admin.register(Tool)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('function', 'unit', 'quantity', 'rate_per_month', 'total_monthly')
    actions = [export_to_excel]  # Add the export action
  
@admin.register(On_Call)
class On_CallAdmin(admin.ModelAdmin):
    list_display = ('type', 'rate', 'no_of_days', 'total')
    actions = [export_to_excel]  # Add the export action
    

@admin.register(CostCalculation)
class CostCalculationAdmin(admin.ModelAdmin):
    list_display = ('cost_category','monthly','y1', 'y2', 'y3' ,'y4','y5')
    actions = [export_to_excel]  # Add the export action



@admin.register(CostSummary)
class CostSummaryAdmin(admin.ModelAdmin):
    list_display = ('customer_name','project_status','contract_duration', 'resource_cost', 'tools' ,'oncall','travel' , 'penalty_risk' , 'total')
    actions = [export_to_excel]  # Add the export action


@admin.register(YearlyCostSummary)
class YearlyCostSummaryAdmin(admin.ModelAdmin):
    list_display = ('customer_name','y1','y2', 'y3', 'y4' ,'y5') 
    actions = [export_to_excel]  # Add the export action