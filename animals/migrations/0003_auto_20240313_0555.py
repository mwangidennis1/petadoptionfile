# Generated by Django 2.2.7 on 2024-03-13 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_animal_animalimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='description',
            field=models.CharField(max_length=800),
        ),
        migrations.CreateModel(
            name='AdoptMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adoptFor', models.CharField(max_length=600)),
                ('caregiver', models.CharField(max_length=100)),
                ('numberofchildren', models.DecimalField(decimal_places=0, max_digits=6)),
                ('allergies', models.CharField(max_length=100)),
                ('residence', models.CharField(max_length=100)),
                ('staydaytime', models.CharField(max_length=100)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adoptme', to='animals.Animal')),
            ],
        ),
    ]
