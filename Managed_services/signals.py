from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ScopingForm, PrivatePublicCloudProjectCost ,Tool ,On_Call,CostCalculation , CostSummary, YearlyCostSummary ,ProjectResourceUtilisation

@receiver(post_save, sender=ScopingForm)
def update_project_costs(sender, instance, created, **kwargs):
    # Get the latest ScopingForm that was just submitted
    scoping_form = instance
    
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

    # Now, populate the ProjectResourceUtilisation table after the ScopingForm is saved
    if created:  # Only append a new entry if it's a new ScopingForm
        ProjectResourceUtilisation.populate_utilisation(scoping_form)