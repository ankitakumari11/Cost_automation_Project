from django.contrib import admin
from .models import ScopingForm ,RateCard,Travel,PrivatePublicCloudProjectCost, Tool,On_Call , CostCalculation ,CostSummary , YearlyCostSummary
# Register your models here.

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


# Register the model with the custom admin class
admin.site.register(ScopingForm, ScopingFormAdmin)


@admin.register(RateCard)
class RateCardAdmin(admin.ModelAdmin):
    list_display = ('role_hr_band','level', 'experience_years', 'partner_rate', 'airtel_rate','responsibility_skills')

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('type', 'unit', 'quantity', 'rate', 'total')


@admin.register(PrivatePublicCloudProjectCost)
class PrivateCloudProjectCostAdmin(admin.ModelAdmin):
    list_display = ('role_level','private_kpi', 'public_kpi', 'unit', 'support_window', 'private_kpi_fte','public_kpi_fte','project_volume','project_fte','rate','total_monthly','complex')

@admin.register(Tool)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('function', 'unit', 'quantity', 'rate_per_month', 'total_monthly')

@admin.register(On_Call)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('type', 'rate', 'no_of_days', 'total')


@admin.register(CostCalculation)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('cost_category','monthly','y1', 'y2', 'y3' ,'y4','y5')


@admin.register(CostSummary)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('customer_name','project_status','contract_duration', 'resource_cost', 'tools' ,'oncall','travel' , 'penalty_risk' , 'total')


@admin.register(YearlyCostSummary)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('customer_name','y1','y2', 'y3', 'y4' ,'y5')