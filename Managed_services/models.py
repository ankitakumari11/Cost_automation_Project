from django.db import models
from django.shortcuts import render, redirect
from decimal import Decimal , ROUND_HALF_UP ,ROUND_CEILING
from django.db.models import Sum
from django.core.validators import MinValueValidator
from django.utils import timezone

#ScopingForm----------------------------------------------------------------------
class ScopingForm(models.Model):
    # Basic Information
    customer_name = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    description = models.TextField(max_length=600, blank=True, null=True ,default="No description provided")
    location = models.CharField(max_length=255 , default="Not specified")
    received_date = models.DateField(default=timezone.now)
    submission_date = models.DateField(default=timezone.now)
    
    PROJECT_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Cancelled', 'Cancelled'),
        ('Closed', 'Closed'),
        ('Dropped', 'Dropped'),
        ('Hold', 'Hold'),
        ('Lost', 'Lost'),
        ('Passive', 'Passive'),
        ('Submitted', 'Submitted'),
        ('Won', 'Won'),
    ]
    project_status = models.CharField(max_length=10, choices=PROJECT_STATUS_CHOICES)
    margin = models.DecimalField(max_digits=10, decimal_places=2)
    penalty_risk = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_windows_vms = models.PositiveIntegerField()
    no_of_linux_vms = models.PositiveIntegerField()
    no_of_rdbms_dbs = models.PositiveIntegerField()
    no_of_nosql_dbs = models.PositiveIntegerField()
    no_of_network_devices = models.PositiveIntegerField()
    Total_VMs_Devices = models.PositiveIntegerField()
    total_storage_capacity = models.DecimalField(max_digits=10, decimal_places=2)  # Capacity in TB
    on_call = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    support_window = models.CharField(max_length=10, choices=[('8x5', '8x5'), ('24x7', '24x7'), ('16x5', '16x5')])
    yoy_increment = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_ad_objects = models.PositiveIntegerField()
    contract_duration = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 11)])  # 1 to 10 years
    dc_type = models.CharField(max_length=20, choices=[('Private Cloud', 'Private Cloud'), ('Public Cloud', 'Public Cloud')])
    no_of_private_cloud_hosts = models.PositiveIntegerField()
    hyper_converged_platform_used = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    dr_in_scope = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    no_of_servers_for_dr = models.PositiveIntegerField()
    dr_drills = models.PositiveIntegerField()
    complexity = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    monitoring = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    patching = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    itsm_services = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    ipc_management_in_scope = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    travel = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    management_governance_support = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    # TCV (in Crore)
    tcv = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="TCV (in Crore)", default=0
    )
    def save(self, *args, **kwargs):
        # Convert fields to integers separately
        no_of_windows_vms = int(self.no_of_windows_vms or 0)
        no_of_linux_vms = int(self.no_of_linux_vms or 0)
        no_of_network_devices = int(self.no_of_network_devices or 0)


        # Calculate the Total_VMs_Devices
        self.Total_VMs_Devices = no_of_windows_vms + no_of_linux_vms + no_of_network_devices

        # Call the parent class's save method
        super().save(*args, **kwargs)

    def __str__(self):
        return self.customer_name

# Rate card-----------------------------------------------------------------
class RateCard(models.Model):
    

    role_hr_band = models.CharField(max_length=50)
    # role_hr_band = models.CharField(max_length=50, choices=ROLE_HR_BAND_CHOICES)
   
    level = models.CharField(max_length=5 , default="NULL")

    experience_years = models.CharField(max_length=20)
    # experience_years = models.CharField(max_length=20 , choices=EXPERIENCE_YEAR_CHOICES)  # Example: '3-5 Years'
    responsibility_skills = models.TextField()
    partner_rate = models.DecimalField(max_digits=10, decimal_places=2)
    airtel_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.role_hr_band


# Travel-----------------------------------------------------------------------------
class Travel(models.Model):
    type = models.CharField(max_length=50)  # Type of travel or service
    unit = models.CharField(max_length=50)  # Example: 'Trips', 'Days', etc.
    quantity = models.IntegerField()  # Normal integer for quantity
    rate = models.DecimalField(max_digits=10, decimal_places=2)  # Rate per unit
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # Total cost, auto-calculated

    def save(self, *args, **kwargs):
        # Calculate the total cost as quantity * rate
        self.total = self.quantity * self.rate
        # Call the parent class's save method
        super().save(*args, **kwargs)

    def __str__(self):
        return self.type

#-----------------------------------Private_Public_CloudProjectCost--------------------------------------

class PrivatePublicCloudProjectCost(models.Model):
    

    role_level = models.CharField(max_length=100)
    private_kpi = models.IntegerField(blank=True, null=True)  # Filled later based on role
    public_kpi = models.IntegerField(blank=True, null=True)   # Filled later based on role
    unit = models.CharField(max_length=50, blank=True, null=True)  # Filled later based on role
    support_window = models.CharField(max_length=10)
    private_kpi_fte = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)  # Filled later based on role
    public_kpi_fte = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)    # Filled later based on role
    project_volume = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2) 
    project_fte = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=5)  # Calculated later
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Can be calculated
    total_monthly = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Calculated later
    complex = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)  

    def save(self, *args, **kwargs):
        # Assume you're using the latest ScopingForm filled in
        scoping_form = ScopingForm.objects.last()

        # Support window
        self.support_window=scoping_form.support_window

        # Conditional logic for Private and Public KPI based on Role - Level and Hyper Converged Platform
        if self.role_level in ['Storage/Backup - F', 'Storage/Backup - E2', 'Storage/Backup - E3']:
            if scoping_form.hyper_converged_platform_used == 'Yes':
                self.private_kpi = 3000
            else:
                self.private_kpi = 1000
               

        # Conditional logic for Private and Public KPI FTE based on Role - Level
        if self.role_level in ['Incident & Problem Manager - E2', 'Change & Release Manager - E2']:
            self.private_kpi_fte = 0.5 if scoping_form.ipc_management_in_scope == 'Yes' else 0
            self.public_kpi_fte = 0.5 if scoping_form.ipc_management_in_scope == 'Yes' else 0
        elif self.role_level in ['Delivery Manager - E4', 'Delivery Head - E6', 'Architect - E4']:
            self.private_kpi_fte = 0.05 if scoping_form.management_governance_support == 'Yes' else 0
            self.public_kpi_fte = 0.05 if scoping_form.management_governance_support == 'Yes' else 0
        elif self.role_level == 'DR Manager - E2':
            self.private_kpi_fte = 0.2 if scoping_form.dr_in_scope == 'Yes' else 0
            self.public_kpi_fte = 0.2 if scoping_form.dr_in_scope == 'Yes' else 0

        # Conditional logic for Project Volume based on Role - Level
        if self.role_level.startswith('Linux Engineer'):
            self.project_volume = scoping_form.no_of_linux_vms  # C9
        elif self.role_level.startswith('Windows Engineer'):
            self.project_volume = scoping_form.no_of_windows_vms  # C7
        elif self.role_level.startswith('Cloud Engineer - OCI Cloud'):
            self.project_volume = scoping_form.no_of_private_cloud_hosts  # C20
        elif self.role_level.startswith('Storage/Backup'):
            self.project_volume = scoping_form.total_storage_capacity  # C14
        elif self.role_level.startswith('Network Engineer'):
            self.project_volume = scoping_form.no_of_network_devices  # C12
        elif self.role_level in ['Terraform/IaaC Automation Engineer - E2', 'Incident & Problem Manager - E2', 'Change & Release Manager - E2', 'Service Desk Lead - B', 'Monitoring/Service Desk Engineer - F']:
            self.project_volume = scoping_form.Total_VMs_Devices  # C13
        elif self.role_level.startswith('RDBMS Admin'):
            self.project_volume = scoping_form.no_of_rdbms_dbs  # C10
        elif self.role_level.startswith('Non-RDBMS Admin'):
            self.project_volume = scoping_form.no_of_nosql_dbs  # C11
        elif self.role_level.startswith('AD Admin'):
            self.project_volume = scoping_form.no_of_ad_objects  # C17
        elif self.role_level in ['Team Lead - E3', 'PMO - E2', 'Delivery Manager - E4', 'Delivery Head - E6', 'Architect - E4']:
            self.project_volume = 0.25 if scoping_form.Total_VMs_Devices >= 300 else 0.13  # C13
        elif self.role_level == 'DR Manager - E2':
            self.project_volume = 1 if scoping_form.no_of_servers_for_dr >= 300 else 0.25  # C23
       
        # Conditional logic for Project FTE calculation
        if scoping_form.dc_type == "Private Cloud":
            kpi=self.private_kpi
            kpi_fte=self.private_kpi_fte
        else:
            kpi=self.public_kpi
            kpi_fte=self.public_kpi_fte

            
        if kpi:
            self.project_fte = (Decimal(self.project_volume) / Decimal(kpi)) * Decimal(kpi_fte)
        else:
            self.project_fte = Decimal(self.project_volume) * Decimal(kpi_fte)

        # Fetch the rate from RateCard model based on role_level
        try:
            rate_card_entry = RateCard.objects.get(role_hr_band=self.role_level)
            self.rate = rate_card_entry.airtel_rate
        except RateCard.DoesNotExist:
            self.rate = Decimal(0)  # Set to 0 if no matching rate is found

        # Total Monthly Calculation
        self.total_monthly = (Decimal(self.project_fte) * Decimal(self.rate))

        # Complex
        self.complex = self.total_monthly * Decimal(1.5)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.role_level} - {self.project_volume} - {self.total_monthly}"

#--------------TOOLS-------------------------------------------

class Tool(models.Model):
    function = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    rate_per_month = models.DecimalField(max_digits=10, decimal_places=5)
    total_monthly = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Fetch the latest ScopingForm instance
        scoping_form = ScopingForm.objects.last()

        # Define the role levels to filter by
        role_levels_to_sum = [
            "Linux Engineer - F", "Linux Engineer - E2", "Linux Engineer - E3",
            "Windows Engineer - F", "Windows Engineer - E2", "Windows Engineer - E3",
            "Cloud Engineer - OCI Cloud - F", "Cloud Engineer - OCI Cloud - E2",
            "Cloud Engineer - OCI Cloud - E3", "Storage/Backup - F", "Storage/Backup - E2",
            "Storage/Backup - E3", "Network Engineer - F", "Network Engineer - E2", 
            "Network Engineer - E3", "Terraform/IaaC Automation Engineer - E2",
            "Incident & Problem Manager - E2", "Change & Release Manager - E2",
            "RDBMS Admin - E2", "RDBMS Admin - E3", "Non-RDBMS Admin - E2",
            "Non-RDBMS Admin - E3", "AD Admin - E2", "AD Admin - E3", 
            "Service Desk Lead - B", "Monitoring/Service Desk Engineer - F", "Team Lead - E3"
        ]

        # Calculate Quantity based on Function and Unit
        if self.function == 'ITSM' and self.unit == 'No of Resolvers':
            # ITSM (No. of Resolver)
            if scoping_form.itsm_services == 'Yes':
                
                    self.quantity = PrivatePublicCloudProjectCost.objects.filter(
                        role_level__in=role_levels_to_sum
                    ).aggregate(total_fte=Sum('project_fte'))['total_fte'] or Decimal(0)
                    
                    # Round Quantity up to the nearest integer
                    self.quantity = self.quantity.quantize(Decimal('1'), rounding=ROUND_CEILING)
                     
            else:
                self.quantity=Decimal(0)

        elif self.function == 'ITSM' and self.unit == 'No of Devices':
            # ITSM (No. of Devices)
            self.quantity = scoping_form.Total_VMs_Devices if scoping_form.itsm_services == 'Yes' else Decimal(0)

        elif self.function == 'Patching' and self.unit == 'Servers':
            # Patching (Servers)
            if scoping_form.patching == 'Yes':
                self.quantity = (
                    int(scoping_form.no_of_windows_vms) +
                    
                    int(scoping_form.no_of_linux_vms)
                )
            else:
                self.quantity = Decimal(0)

        elif self.function == 'ELK' and self.unit == 'Servers':
            # ELK (Servers)
            self.quantity = scoping_form.Total_VMs_Devices if scoping_form.monitoring == 'Yes' else Decimal(0)

        # Calculate Total Monthly based on Quantity and Rate/Month
        if self.quantity is not None and self.rate_per_month is not None:
            self.total_monthly = self.quantity * self.rate_per_month

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.function} - {self.unit} - {self.total_monthly}"
    


#----------------------ON_CALL--------------------------------------

class On_Call(models.Model):
    TYPE_CHOICES = [
        ('Weekday', 'Weekday'),
        ('Weekend', 'Weekend'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_days = models.PositiveIntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Fetch the latest ScopingForm instance
        scoping_form = ScopingForm.objects.latest('id')


        if scoping_form:
            # Set no_of_days based on type and Total VMs + Devices
            if self.type == 'Weekend':
                self.no_of_days = 8 if scoping_form.Total_VMs_Devices > 150 else 0
            elif self.type == 'Weekday':
                self.no_of_days = 22 if scoping_form.Total_VMs_Devices > 150 else 10
            
            # Calculate the total
            self.total = self.rate * Decimal(self.no_of_days)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type} - {self.rate} - {self.no_of_days}"


#---------------CALCULATION TABLE------------------------------------------------
class CostCalculation(models.Model):
    cost_category = models.CharField(max_length=50, unique=True)
    monthly = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    y1 = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    y2 = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    y3 = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    y4 = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    y5 = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.cost_category

    @staticmethod
    def calculate_values():
        """
        Calculate and update values based on the complexity level from the latest ScopingForm.
        """
        # Fetch the latest ScopingForm data
        scoping_form = ScopingForm.objects.last()
        complexity_level = scoping_form.complexity  # Assuming 'complexity_level' field exists in ScopingForm
    

        # Retrieve values from related models
        private_public_cost_sum = PrivatePublicCloudProjectCost.objects.aggregate(total=models.Sum('total_monthly'))['total'] or Decimal('0.00')
       
        tools_total = Tool.objects.aggregate(total=models.Sum('total_monthly'))['total'] or Decimal('0.00')
        
        on_call_total = On_Call.objects.aggregate(total=models.Sum('total'))['total'] if scoping_form.on_call == 'Yes' else Decimal('0.00')
        
        travel_total = Travel.objects.aggregate(total=models.Sum('total'))['total'] if scoping_form.travel == 'Yes' else Decimal('0.00')
        

        # Constants from ScopingForm
        margin_percent = Decimal(scoping_form.margin) / 100
        penalty_risk_percent = Decimal(scoping_form.penalty_risk) / 100
        contract_duration = scoping_form.contract_duration
        yoy_increment = Decimal(scoping_form.yoy_increment) / 100

        # Adjust factors based on complexity level
        resources_cost = Decimal('0.00')
        tools_multiplier = Decimal('0.00')
        if complexity_level.lower() == 'low':
            tools_multiplier = Decimal('1.0')
            resources_cost = private_public_cost_sum
            
        elif complexity_level.lower() == 'medium':
            tools_multiplier = Decimal('1.25')
            resources_cost = private_public_cost_sum + (private_public_cost_sum * Decimal('0.25'))
          
        elif complexity_level.lower() == 'high':
            tools_multiplier = Decimal('1.5')
            resources_cost = private_public_cost_sum + ((private_public_cost_sum + (private_public_cost_sum * Decimal('0.25'))) * Decimal('0.4'))
            

        # Calculate Monthly values for each category
        monthly_values = {
            'Resources Cost': resources_cost,
            'Tools': tools_total * tools_multiplier,
            'OnCall': on_call_total,
            'Travel': travel_total,
        }
        monthly_values['Overhead'] = monthly_values['Resources Cost'] * Decimal('0.05')
        monthly_values['Margin'] = sum(monthly_values.values()) * margin_percent

        monthly_values['Penalty Risk'] = (monthly_values['Resources Cost']+monthly_values['Tools']+monthly_values['OnCall']+monthly_values['Travel']+monthly_values['Overhead']+monthly_values['Margin']) * penalty_risk_percent
        monthly_values['Sum'] = sum(monthly_values.values())


        # Define all required cost categories
        required_categories = ['Resources Cost', 'Tools', 'OnCall', 'Travel', 'Overhead', 'Margin', 'Penalty Risk', 'Sum']

        # Initialize yearly values with all required categories set to 0 for each year
        yearly_values = {f'y{year}': {category: Decimal('0.00') for category in required_categories} for year in range(1, 6)}

        # Calculate yearly values based on contract duration and assign calculated values
        for year in range(1, 6):
            if contract_duration >= year:
                if year == 1:
                    yearly_values['y1'] = {key: value * 12 for key, value in monthly_values.items()}
                    yearly_values['y1']['Travel'] = monthly_values['Travel'] * 3
                    # Calculate Overhead, Margin, and Penalty Risk for y1
                    yearly_values['y1']['Overhead'] = yearly_values['y1']['Resources Cost'] * Decimal('0.05')
                    yearly_values['y1']['Margin'] = (yearly_values['y1']['Resources Cost'] +
                                  yearly_values['y1']['Tools'] +
                                  yearly_values['y1']['OnCall'] +
                                  yearly_values['y1']['Travel'] +
                                  yearly_values['y1']['Overhead']) * margin_percent
                    
                   
                    yearly_values['y1']['Penalty Risk'] = (yearly_values['y1']['Resources Cost'] +
                                  yearly_values['y1']['Tools'] +
                                  yearly_values['y1']['OnCall'] +
                                  yearly_values['y1']['Travel'] +
                                  yearly_values['y1']['Overhead'] +
                                  yearly_values['y1']['Margin']) * penalty_risk_percent

                        # Calculate final Sum after all components are added
                    yearly_values['y1']['Sum'] = (yearly_values['y1']['Resources Cost'] +
                                  yearly_values['y1']['Tools'] +
                                  yearly_values['y1']['OnCall'] +
                                  yearly_values['y1']['Travel'] +
                                  yearly_values['y1']['Overhead'] +
                                  yearly_values['y1']['Margin'] +
                                  yearly_values['y1']['Penalty Risk'])

                else:
                    previous_year = f'y{year - 1}'
                    yearly_values[f'y{year}'] = {
                        'Resources Cost': yearly_values[previous_year]['Resources Cost'] * (1 + yoy_increment),
                        'Tools': yearly_values[previous_year]['Tools'] * Decimal('1.03'),
                        'OnCall': yearly_values[previous_year]['OnCall'],
                        'Travel': yearly_values[previous_year]['Travel'],
                    }

                    
                    yearly_values[f'y{year}']['Overhead'] = yearly_values[f'y{year}']['Resources Cost'] * Decimal('0.05')
                    

                    yearly_values[f'y{year}']['Margin'] = (yearly_values[f'y{year}']['Resources Cost'] +
                                  yearly_values[f'y{year}']['Tools'] +
                                  yearly_values[f'y{year}']['OnCall'] +
                                  yearly_values[f'y{year}']['Travel'] +
                                  yearly_values[f'y{year}']['Overhead']) * margin_percent


                    yearly_values[f'y{year}']['Penalty Risk'] = (yearly_values[f'y{year}']['Resources Cost'] +
                                  yearly_values[f'y{year}']['Tools'] +
                                  yearly_values[f'y{year}']['OnCall'] +
                                  yearly_values[f'y{year}']['Travel'] +
                                  yearly_values[f'y{year}']['Overhead']+
                                  yearly_values[f'y{year}']['Margin']) * penalty_risk_percent

                    

                    yearly_values[f'y{year}']['Sum'] = sum(yearly_values[f'y{year}'].values())

        
        
                
        # Calculate final cost after calculating yearly values
        final_cost = sum(yearly_values[f'y{year}']['Sum'] for year in range(1,6)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        if(scoping_form.support_window=='16x5'):
            final_cost=final_cost*Decimal("1.5")
        elif (scoping_form.support_window=='24x7'):
            final_cost=final_cost*Decimal("2")
        else:
            final_cost=final_cost


        # Update CostCalculation records with calculated values
        for category, monthly_value in monthly_values.items():
            cost_calculation, created = CostCalculation.objects.get_or_create(cost_category=category)
            cost_calculation.monthly = monthly_value
            for year in range(1, 6):
                year_key = f'y{year}'
                if year_key in yearly_values and category in yearly_values[year_key]:
                    setattr(cost_calculation, year_key, yearly_values[year_key][category])
            cost_calculation.save()

        return final_cost

    
class CostSummary(models.Model):
    customer_name = models.CharField(max_length=255)
    project_status = models.CharField(max_length=50)
    contract_duration = models.IntegerField()
    resource_cost = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    tools = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    oncall = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    travel = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    penalty_risk = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    total = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"Cost Summary for {self.customer_name} - {self.project_status}"

    @staticmethod
    def populate_cost_summary():
        # Get the most recent ScopingForm
        scoping_form = ScopingForm.objects.last()

        # Retrieve the values from the CostCalculation table for each cost category
        cost_categories = ['Resources Cost', 'Tools', 'OnCall', 'Travel', 'Penalty Risk', 'Sum']

        # Initialize sums for each category
        resource_cost = Decimal('0.00')
        tools = Decimal('0.00')
        oncall = Decimal('0.00')
        travel = Decimal('0.00')
        penalty_risk = Decimal('0.00')
        total = Decimal('0.00')

        # Loop through the cost categories and calculate the sum of Y1 to Y5
        for category in cost_categories:
            cost_calculation = CostCalculation.objects.filter(cost_category=category)
            for calc in cost_calculation:
                for year in range(1, 6):
                    # Accumulate the values for each year (Y1 to Y5) and category
                    value = getattr(calc, f'y{year}', Decimal('0.00'))
                    if category == 'Resources Cost':
                        resource_cost += value
                    elif category == 'Tools':
                        tools += value
                    elif category == 'OnCall':
                        oncall += value
                    elif category == 'Travel':
                        travel += value
                    elif category == 'Penalty Risk':
                        penalty_risk += value
                    elif category == 'Sum':
                        total += value

        # Now use the ScopingForm data to fill in fields for customer_name, project_status, contract_duration
        customer_name = scoping_form.customer_name
        project_status = scoping_form.project_status
        contract_duration = scoping_form.contract_duration

        # Create and save the new CostSummary entry
        cost_summary = CostSummary(
            customer_name=customer_name,
            project_status=project_status,
            contract_duration=contract_duration,
            resource_cost=resource_cost,
            tools=tools,
            oncall=oncall,
            travel=travel,
            penalty_risk=penalty_risk,
            total=total
        )
        cost_summary.save()
    
class YearlyCostSummary(models.Model):
    customer_name = models.CharField(max_length=255)
    y1 = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    y2 = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    y3 = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    y4 = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    y5 = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"Yearly Cost Summary for {self.customer_name}"

    @staticmethod
    def populate_yearly_cost_summary():
        # Get the most recent ScopingForm
        scoping_form = ScopingForm.objects.last()
        customer_name = scoping_form.customer_name if scoping_form else "Unknown Customer"

        # Fetch the "Sum" row from the CostCalculation table
        sum_row = CostCalculation.objects.filter(cost_category="Sum").first()
        
        # If "Sum" row exists, use its values for y1 to y5; otherwise, default to zero
        yearly_cost_summary = YearlyCostSummary(
            customer_name=customer_name,
            y1=getattr(sum_row, 'y1', Decimal('0.00')),
            y2=getattr(sum_row, 'y2', Decimal('0.00')),
            y3=getattr(sum_row, 'y3', Decimal('0.00')),
            y4=getattr(sum_row, 'y4', Decimal('0.00')),
            y5=getattr(sum_row, 'y5', Decimal('0.00'))
        )

        # Save the new YearlyCostSummary entry
        yearly_cost_summary.save()
   