from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid

class Animal(models.Model):
    id = models.UUIDField( 
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False)
    title=models.CharField(max_length=200)
    breed=models.CharField(max_length=200)
    sex=models.CharField(max_length=200)
    age=models.DecimalField(max_digits=6,decimal_places=0)
    color=models.CharField(max_length=200)
    size=models.CharField(max_length=200)
    description=models.CharField(max_length=800)
    animalimage=models.ImageField(upload_to='covers/',blank=True)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('animal_detail',args=[str(self.id)])

class AdoptMe(models.Model):
    animal=models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name='adoptme',
    )
    adoptFor=models.CharField(max_length=600)
    caregiver=models.CharField(max_length=100)
    numberofchildren=models.DecimalField(max_digits=6,decimal_places=0)
    allergies=models.CharField(max_length=100)
    residence=models.CharField(max_length=100)
    staydaytime=models.CharField(max_length=100)

    def __str__(self):
        return self.animal

