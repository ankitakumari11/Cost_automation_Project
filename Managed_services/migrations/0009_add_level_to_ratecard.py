# 0009_add_level_to_ratecard.py

from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('Managed_services', '0008_alter_privatecloudprojectcost_project_fte_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratecard',
            name='level',
            field=models.CharField(default='NULL', max_length=5),
        ),
    ]
