from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView
from .models import Animal,AdoptMe

class AnimalListView(TemplateView):
    model=Animal
    context_object_name = 'animal_list'
    template_name='animals/animals_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animal_list'] = Animal.objects.all()
        #print(context)  
        return context

class AnimalDetailView(DetailView):
    model=Animal
    context_object_name = 'animal'
    template_name='animals/animal_detail.html'

class AnimalAdoptView(TemplateView):
    model=AdoptMe
    context_object_name='animal_adopt'
    template_name='animals/adopt_me.html'   


