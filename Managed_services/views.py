from django.shortcuts import render, redirect ,get_object_or_404
from django.http import JsonResponse
from .models import CostCalculation, ScopingForm , CostSummary ,RateCard, Travel, PrivatePublicCloudProjectCost, Tool, On_Call, CostCalculation
import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.styles import Border, Side
from django.http import HttpResponse



def export_all_data(request):
    # Fetch the latest ScopingForm instance
    scoping_form = ScopingForm.objects.last()  # Change this logic as per your requirements
    customer_name = scoping_form.customer_name if scoping_form else "default"

    # Create a new workbook
    workbook = openpyxl.Workbook()
    del workbook['Sheet']  # Remove the default sheet

    # Define a border style
    border = Border(
        left=Side(border_style='thin', color='000000'),
        right=Side(border_style='thin', color='000000'),
        top=Side(border_style='thin', color='000000'),
        bottom=Side(border_style='thin', color='000000')
    )

    # Add ScopingForm data in a new sheet (transposed)
    if scoping_form:
        scoping_form_sheet = workbook.create_sheet(title="ScopingForm")
        
        # Write field names in the first column and corresponding values in the second column (transpose)
        scoping_form_fields = [field.name for field in ScopingForm._meta.fields if field.name != "id"]  # Exclude 'id'
        
        for row_num, field_name in enumerate(scoping_form_fields, start=1):
            scoping_form_sheet[f"A{row_num}"] = field_name  # Field name in the first column
            value = getattr(scoping_form, field_name)
            scoping_form_sheet[f"B{row_num}"] = value  # Corresponding value in the second column
            # Apply border to each cell
            scoping_form_sheet[f"A{row_num}"].border = border
            scoping_form_sheet[f"B{row_num}"].border = border

    # Add data for each table
    model_sheets = {
        "CostCalculation": CostCalculation,
        "PrivatePublicCloudProjectCost": PrivatePublicCloudProjectCost,
        "Tools": Tool,
        "RateCard": RateCard,
        "Travel": Travel,      
        "On_Call": On_Call,
        
    }

    for sheet_name, model in model_sheets.items():
        sheet = workbook.create_sheet(title=sheet_name)

        # Get all objects and their fields
        objects = model.objects.all()
        if objects.exists():
            fields = [field.name for field in model._meta.fields if field.name != "id"]  # Exclude 'id'

            # Write headers and apply borders
            for col_num, field_name in enumerate(fields, start=1):
                col_letter = get_column_letter(col_num)
                sheet[f"{col_letter}1"] = field_name
                sheet[f"{col_letter}1"].border = border  # Apply border to header

            # Write rows and apply borders
            for row_num, obj in enumerate(objects, start=2):
                for col_num, field_name in enumerate(fields, start=1):
                    col_letter = get_column_letter(col_num)
                    value = getattr(obj, field_name)
                    cell = sheet[f"{col_letter}{row_num}"]
                    cell.value = value
                    cell.border = border  # Apply border to each cell

    

    # Use customer_name in the filename, ensuring it's safe for a file name
    sanitized_customer_name = "".join(c if c.isalnum() or c in (' ', '_') else "_" for c in customer_name).strip()
    filename = f"{sanitized_customer_name}_data.xlsx"

    # Save workbook to response
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f"attachment; filename={filename}"
    workbook.save(response)
    return response





# def scoping_form(request):
#     if request.method == 'POST':
#         # Retrieve form data from the POST request
#         customer_name = request.POST.get('CustomerName')
#         project_name = request.POST.get('ProjectName')
#         description = request.POST.get('Description')
#         location = request.POST.get('Location')
#         received_date = request.POST.get('ReceivedDate')
#         submission_date = request.POST.get('SubmissionDate')
#         project_status = request.POST.get('ProjectStatus')
#         margin = request.POST.get('Margin')
#         penalty_risk = request.POST.get('PenaltyRisk')
#         no_of_windows_vms = request.POST.get('WindowsVM')
#         no_of_linux_vms = request.POST.get('LinuxVM')
#         no_of_rdbms_dbs = request.POST.get('RDBMdB')
#         no_of_nosql_dbs = request.POST.get('NOSQLdB')
#         no_of_network_devices = request.POST.get('NetworkDevices')
#         Total_VMs_Devices = request.POST.get('Total_VMs_Devices')
#         total_storage_capacity = request.POST.get('StorageCapacity')
#         on_call = request.POST.get('OnCall')
#         support_window = request.POST.get('SupportWindow')
#         yoy_increment = request.POST.get('YoYIncrement')
#         no_of_ad_objects = request.POST.get('noOfAD')
#         contract_duration = request.POST.get('ContractDuration')
#         dc_type = request.POST.get('TypeOfDC')
#         no_of_private_cloud_hosts = request.POST.get('PriavteCloudHosts')
#         hyper_converged_platform_used = request.POST.get('ConvergedPlatform')
#         dr_in_scope = request.POST.get('DRInScope')
#         no_of_servers_for_dr = request.POST.get('ServersforDR')
#         dr_drills = request.POST.get('DRdrills')
#         complexity = request.POST.get('Complexity')
#         monitoring = request.POST.get('Monitoring')
#         patching = request.POST.get('Patching')
#         itsm_services = request.POST.get('ITSMservices')
#         ipc_management_in_scope = request.POST.get('IPCManagement')
#         travel = request.POST.get('Travel')
#         management_governance_support = request.POST.get('GovernanceSupport')
#         tcv = request.POST.get('TCV')

#         # Create a new ScopingForm instance and save it
#         scoping_form_instance = ScopingForm(
#             customer_name=customer_name,
#             project_name=project_name,
#             description=description,
#             location=location,
#             received_date=received_date,
#             submission_date=submission_date,
#             project_status=project_status,
#             margin=margin,
#             penalty_risk=penalty_risk,
#             no_of_windows_vms=no_of_windows_vms,
#             no_of_linux_vms=no_of_linux_vms,
#             no_of_rdbms_dbs=no_of_rdbms_dbs,
#             no_of_nosql_dbs=no_of_nosql_dbs,
#             no_of_network_devices=no_of_network_devices,
#             Total_VMs_Devices=Total_VMs_Devices,
#             total_storage_capacity=total_storage_capacity,
#             on_call=on_call,
#             support_window=support_window,
#             yoy_increment=yoy_increment,
#             no_of_ad_objects=no_of_ad_objects,
#             contract_duration=contract_duration,
#             dc_type=dc_type,
#             no_of_private_cloud_hosts=no_of_private_cloud_hosts,
#             hyper_converged_platform_used=hyper_converged_platform_used,
#             dr_in_scope=dr_in_scope,
#             no_of_servers_for_dr=no_of_servers_for_dr,
#             dr_drills=dr_drills,
#             complexity=complexity,
#             monitoring=monitoring,
#             patching=patching,
#             itsm_services=itsm_services,
#             ipc_management_in_scope=ipc_management_in_scope,
#             travel=travel,
#             management_governance_support=management_governance_support,
#             tcv=tcv
#         )
#         scoping_form_instance.save()

#         final_cost = CostCalculation.calculate_values()

        
#         cost_summary = CostSummary.objects.last()


#         return render(request, 'home.html', {'final_cost': final_cost ,'cost_summary': cost_summary})

   
#     return render(request, 'home.html')



#################3
# def scoping_form(request):
#     # Check if the form has been submitted (POST request)
#     if request.method == 'POST':
#         # If the form has already been submitted in the current session, skip the processing
#         if request.session.get('form_submitted', False):
#             # Render the page without saving the form again
#             final_cost = None
#             cost_summary = None
#             return render(request, 'home.html', {'final_cost': final_cost, 'cost_summary': cost_summary})
        
#         # Retrieve form data from the POST request
#         customer_name = request.POST.get('CustomerName')
#         project_name = request.POST.get('ProjectName')

#         # Check if the ScopingForm already exists to avoid duplicates
#         existing_form = ScopingForm.objects.filter(customer_name=customer_name, project_name=project_name).first()

#         if not existing_form:  # Only create a new instance if it doesn't exist
#             scoping_form_instance = ScopingForm(
#                 customer_name=customer_name,
#                 project_name=project_name,
#                 description=request.POST.get('Description'),
#                 location=request.POST.get('Location'),
#                 received_date=request.POST.get('ReceivedDate'),
#                 submission_date=request.POST.get('SubmissionDate'),
#                 project_status=request.POST.get('ProjectStatus'),
#                 margin=request.POST.get('Margin'),
#                 penalty_risk=request.POST.get('PenaltyRisk'),
#                 no_of_windows_vms=request.POST.get('WindowsVM'),
#                 no_of_linux_vms=request.POST.get('LinuxVM'),
#                 no_of_rdbms_dbs=request.POST.get('RDBMdB'),
#                 no_of_nosql_dbs=request.POST.get('NOSQLdB'),
#                 no_of_network_devices=request.POST.get('NetworkDevices'),
#                 Total_VMs_Devices=request.POST.get('Total_VMs_Devices'),
#                 total_storage_capacity=request.POST.get('StorageCapacity'),
#                 on_call=request.POST.get('OnCall'),
#                 support_window=request.POST.get('SupportWindow'),
#                 yoy_increment=request.POST.get('YoYIncrement'),
#                 no_of_ad_objects=request.POST.get('noOfAD'),
#                 contract_duration=request.POST.get('ContractDuration'),
#                 dc_type=request.POST.get('TypeOfDC'),
#                 no_of_private_cloud_hosts=request.POST.get('PriavteCloudHosts'),
#                 hyper_converged_platform_used=request.POST.get('ConvergedPlatform'),
#                 dr_in_scope=request.POST.get('DRInScope'),
#                 no_of_servers_for_dr=request.POST.get('ServersforDR'),
#                 dr_drills=request.POST.get('DRdrills'),
#                 complexity=request.POST.get('Complexity'),
#                 monitoring=request.POST.get('Monitoring'),
#                 patching=request.POST.get('Patching'),
#                 itsm_services=request.POST.get('ITSMservices'),
#                 ipc_management_in_scope=request.POST.get('IPCManagement'),
#                 travel=request.POST.get('Travel'),
#                 management_governance_support=request.POST.get('GovernanceSupport'),
#                 tcv=request.POST.get('TCV')
#             )
#             scoping_form_instance.save()

#             # Mark the form as submitted in the session
#             request.session['form_submitted'] = True

#             # Trigger calculation of final cost
#             final_cost = CostCalculation.calculate_values()

#             # Get the last CostSummary entry
#             cost_summary = CostSummary.objects.last()

#             return render(request, 'home.html', {'final_cost': final_cost, 'cost_summary': cost_summary})

#     else:
#         # If GET request, reset session flag and cost summary
#         if 'form_submitted' in request.session:
#             # Clear the session flag to allow new submissions in future
#             del request.session['form_submitted']

#         final_cost = None
#         cost_summary = None

#         return render(request, 'home.html', {'final_cost': final_cost, 'cost_summary': cost_summary})




#############3

def scoping_form(request):
    # Check if the form has been submitted (POST request)
    if request.method == 'POST':
        # Retrieve form data from the POST request
        customer_name = request.POST.get('CustomerName')
        project_name = request.POST.get('ProjectName')

        # Check if the ScopingForm already exists to avoid duplicates
        existing_form = ScopingForm.objects.filter(customer_name=customer_name, project_name=project_name).first()

        if not existing_form:  # Only create a new instance if it doesn't exist
            # Create the new ScopingForm instance
            scoping_form_instance = ScopingForm(
                customer_name=customer_name,
                project_name=project_name,
                description=request.POST.get('Description'),
                location=request.POST.get('Location'),
                received_date=request.POST.get('ReceivedDate'),
                submission_date=request.POST.get('SubmissionDate'),
                project_status=request.POST.get('ProjectStatus'),
                margin=request.POST.get('Margin'),
                penalty_risk=request.POST.get('PenaltyRisk'),
                no_of_windows_vms=request.POST.get('WindowsVM'),
                no_of_linux_vms=request.POST.get('LinuxVM'),
                no_of_rdbms_dbs=request.POST.get('RDBMdB'),
                no_of_nosql_dbs=request.POST.get('NOSQLdB'),
                no_of_network_devices=request.POST.get('NetworkDevices'),
                Total_VMs_Devices=request.POST.get('Total_VMs_Devices'),
                total_storage_capacity=request.POST.get('StorageCapacity'),
                on_call=request.POST.get('OnCall'),
                support_window=request.POST.get('SupportWindow'),
                yoy_increment=request.POST.get('YoYIncrement'),
                no_of_ad_objects=request.POST.get('noOfAD'),
                contract_duration=request.POST.get('ContractDuration'),
                dc_type=request.POST.get('TypeOfDC'),
                no_of_private_cloud_hosts=request.POST.get('PriavteCloudHosts'),
                hyper_converged_platform_used=request.POST.get('ConvergedPlatform'),
                dr_in_scope=request.POST.get('DRInScope'),
                no_of_servers_for_dr=request.POST.get('ServersforDR'),
                dr_drills=request.POST.get('DRdrills'),
                complexity=request.POST.get('Complexity'),
                monitoring=request.POST.get('Monitoring'),
                patching=request.POST.get('Patching'),
                itsm_services=request.POST.get('ITSMservices'),
                ipc_management_in_scope=request.POST.get('IPCManagement'),
                travel=request.POST.get('Travel'),
                management_governance_support=request.POST.get('GovernanceSupport'),
                tcv=request.POST.get('TCV')
            )
            scoping_form_instance.save()

            # Mark the form as submitted in the session
            request.session['form_submitted'] = True

            # Trigger calculation of final cost
            final_cost = CostCalculation.calculate_values()

            # Get the last CostSummary entry
            cost_summary = CostSummary.objects.last()

            return render(request, 'home.html', {'final_cost': final_cost, 'cost_summary': cost_summary})

        else:
            # If the form already exists, you can either notify the user or redirect them
            return render(request, 'home.html', {'error': 'This project and customer already exist in the database.'})

    else:
        # If GET request (i.e., the user is loading the page or refreshing):
        # Reset session flag to allow future submissions
        if 'form_submitted' in request.session:
            del request.session['form_submitted']

        # Reset final_cost and cost_summary to None on initial load or page reload
        final_cost = None
        cost_summary = None

        return render(request, 'home.html', {'final_cost': final_cost, 'cost_summary': cost_summary})