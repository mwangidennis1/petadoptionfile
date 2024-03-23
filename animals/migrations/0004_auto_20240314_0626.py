# Generated by Django 2.2.7 on 2024-03-14 06:26
import os
from django.db import migrations,models
import json
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Migration(migrations.Migration):
    '''def seed_data(apps,schema_editor):
        Animal=apps.get_model("animals","Animal")
        #json_path=os.path.join(BASE_DIR,'animal_data.json')
        with open('/petadoption/animal_data.json','r',encoding='utf-16') as file:
            data=json.load(file)
        for item in data:
            valid_fields = {key: value for key, value in item.items() if key in Animal._meta.fields}
            animal=Animal(**valid_fields)
            animal.save()'''


    dependencies = [
        ('animals', '0003_auto_20240313_0555'),
    ]

    operations = [
        #migrations.RunPython(seed_data),
         migrations.AlterField(
            model_name='animal',
            name='age',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6),
        ),
    ]
