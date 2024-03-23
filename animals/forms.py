from django import forms
from .models import AdoptMe,Animal

class AdoptMeForm(forms.ModelForm):
     
    class Meta:
        model = AdoptMe
        fields = ['adoptFor','caregiver','numberofchildren','allergies','residence','staydaytime']    
    def __init__(self, *args, **kwargs):
        # Get the Animal instance from the initial data if provided
        initial_animal = kwargs.pop('initial_animal', None)
        super().__init__(*args, **kwargs)
        # Set the initial value for the animal field if an instance is provided
        if initial_animal:
            self.fields['animal'].initial = initial_animal
            self.fields['animal'].widget.attrs['readonly'] = True  # Optional: Make the field readonly