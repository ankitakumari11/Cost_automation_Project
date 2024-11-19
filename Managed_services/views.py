from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import CostCalculation, ScopingForm

# Create your views here.
from django.shortcuts import render, redirect
from .models import ScopingForm

def scoping_form(request):
    if request.method == 'POST':
        # Retrieve form data from the POST request
        customer_name = request.POST.get('CustomerName')
        project_name = request.POST.get('ProjectName')
        description = request.POST.get('Description')
        location = request.POST.get('Location')
        received_date = request.POST.get('ReceivedDate')
        submission_date = request.POST.get('SubmissionDate')
        project_status = request.POST.get('ProjectStatus')
        margin = request.POST.get('Margin')
        penalty_risk = request.POST.get('PenaltyRisk')
        no_of_windows_vms = request.POST.get('WindowsVM')
        no_of_linux_vms = request.POST.get('LinuxVM')
        no_of_rdbms_dbs = request.POST.get('RDBMdB')
        no_of_nosql_dbs = request.POST.get('NOSQLdB')
        no_of_network_devices = request.POST.get('NetworkDevices')
        Total_VMs_Devices = request.POST.get('Total_VMs_Devices')
        total_storage_capacity = request.POST.get('StorageCapacity')
        on_call = request.POST.get('OnCall')
        support_window = request.POST.get('SupportWindow')
        yoy_increment = request.POST.get('YoYIncrement')
        no_of_ad_objects = request.POST.get('noOfAD')
        contract_duration = request.POST.get('ContractDuration')
        dc_type = request.POST.get('TypeOfDC')
        no_of_private_cloud_hosts = request.POST.get('PriavteCloudHosts')
        hyper_converged_platform_used = request.POST.get('ConvergedPlatform')
        dr_in_scope = request.POST.get('DRInScope')
        no_of_servers_for_dr = request.POST.get('ServersforDR')
        dr_drills = request.POST.get('DRdrills')
        complexity = request.POST.get('Complexity')
        monitoring = request.POST.get('Monitoring')
        patching = request.POST.get('Patching')
        itsm_services = request.POST.get('ITSMservices')
        ipc_management_in_scope = request.POST.get('IPCManagement')
        travel = request.POST.get('Travel')
        management_governance_support = request.POST.get('GovernanceSupport')
        tcv = request.POST.get('TCV')

        # Create a new ScopingForm instance and save it
        scoping_form_instance = ScopingForm(
            customer_name=customer_name,
            project_name=project_name,
            description=description,
            location=location,
            received_date=received_date,
            submission_date=submission_date,
            project_status=project_status,
            margin=margin,
            penalty_risk=penalty_risk,
            no_of_windows_vms=no_of_windows_vms,
            no_of_linux_vms=no_of_linux_vms,
            no_of_rdbms_dbs=no_of_rdbms_dbs,
            no_of_nosql_dbs=no_of_nosql_dbs,
            no_of_network_devices=no_of_network_devices,
            Total_VMs_Devices=Total_VMs_Devices,
            total_storage_capacity=total_storage_capacity,
            on_call=on_call,
            support_window=support_window,
            yoy_increment=yoy_increment,
            no_of_ad_objects=no_of_ad_objects,
            contract_duration=contract_duration,
            dc_type=dc_type,
            no_of_private_cloud_hosts=no_of_private_cloud_hosts,
            hyper_converged_platform_used=hyper_converged_platform_used,
            dr_in_scope=dr_in_scope,
            no_of_servers_for_dr=no_of_servers_for_dr,
            dr_drills=dr_drills,
            complexity=complexity,
            monitoring=monitoring,
            patching=patching,
            itsm_services=itsm_services,
            ipc_management_in_scope=ipc_management_in_scope,
            travel=travel,
            management_governance_support=management_governance_support,
            tcv=tcv
        )
        scoping_form_instance.save()

        final_cost = CostCalculation.calculate_values()


        return render(request, 'home.html', {'final_cost': final_cost})


    return render(request, 'home.html')


