from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver
from .models import ScopingForm, PrivatePublicCloudProjectCost ,Tool ,On_Call,CostCalculation , CostSummary, YearlyCostSummary ,ProjectResourceUtilisation
from .utils import set_current_project_name

@receiver(post_save, sender=ScopingForm)
def update_project_costs(sender, instance, created, **kwargs):
    # Get the latest ScopingForm that was just submitted
    scoping_form = instance
    # Set the project_name in the thread-local storage
    set_current_project_name(instance.project_name)


    # if created:
    #     # Handle logic for a newly created ScopingForm if needed
    #     print("New project created:", scoping_form.project_name)
    #     print("New customer_name created:", scoping_form.customer_name)

    # else:
    #     # This is an update to an existing ScopingForm, so we can use the updated data
    #     print("Updated project:", scoping_form.project_name)
    #     print("Updated customer_name:", scoping_form.customer_name)

    # Print all values of the scoping_form
    print("\nAll fields of the updated ScopingForm:")
    for field in scoping_form._meta.fields:
        field_name = field.name
        field_value = getattr(scoping_form, field_name, 'N/A')  # Fetch the value of each field
        

    
    # Get all existing records in PrivateCloudProjectCost
    project_costs = PrivatePublicCloudProjectCost.objects.all()

    # Loop through each record and update it based on the new ScopingForm
    for project_cost in project_costs:
        # Logic already in models.py will calculate and update each project cost
        project_cost.save()

    # Update all existing records in Tools
    tools_entries = Tool.objects.all()
    for tool in tools_entries:
        # The save method in Tools already includes calculation logic for quantity and total_monthly
        tool.save()

     # Update all existing records in Tools
    On_Call_entries = On_Call.objects.all()
    for on_Call in On_Call_entries:
        on_Call.save()

    # Recalculate and update CostCalculation records
    CostCalculation.calculate_values()

    # Populate the CostSummary table after recalculating all costs
    CostSummary.populate_cost_summary()

    YearlyCostSummary.populate_yearly_cost_summary()

    ProjectResourceUtilisation.populate_utilisation(scoping_form)


    # Now, populate the ProjectResourceUtilisation table after the ScopingForm is saved
    # if created:  # Only append a new entry if it's a new ScopingForm
    #     ProjectResourceUtilisation.populate_utilisation(scoping_form)


@receiver(post_delete, sender=ScopingForm)
def delete_related_data(sender, instance, **kwargs):
    project_name = instance.project_name

    # Explicitly delete related records in other tables
    YearlyCostSummary.objects.filter(project_name=project_name).delete()
    ProjectResourceUtilisation.objects.filter(project_name=project_name).delete()
    CostSummary.objects.filter(project_name=project_name).delete()

    print(f"Deleted related data for project: {project_name}")