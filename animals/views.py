from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView,TemplateView
from .models import Animal,AdoptMe
from django.views.generic.edit import CreateView 
from .forms import AdoptMeForm
from django.urls import reverse
from django.http import Http404
from django.http import JsonResponse 
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
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

class AnimalAdoptView(LoginRequiredMixin,CreateView):
    model=AdoptMe
    template_name='animals/adopt_me.html' 
    fields=['adoptFor','caregiver','numberofchildren','allergies','residence','staydaytime']
    login_url = 'account_login' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch the Animal object based on the animal_id from the URL
        animal_id = self.kwargs.get('animal_id')
        animal = Animal.objects.get(id=animal_id)
        context['animal'] = animal
        return context
def adopt_me_view(request):
    if request.method == 'POST':
        # Create a form instance with the POST data
        form = AdoptMeForm(request.POST)
        if form.is_valid():
            form.instance.animal_id = request.POST.get('animal_id') 
            # If the form is valid, save the data to the AdoptMe model
            adopt_me_instance = form.save()
            # Optionally, perform any additional processing or redirect to a success page
            return redirect('/success_form')  # Replace 'success_url' with the URL to redirect after successful form submission
    else:
        # If the request method is GET, create an empty form instance
        form = AdoptMeForm()
    
    # Render the template with the form
    return render(request, 'adopt_me.html', {'form': form})

class SearchResultListView(ListView):
    model=Animal
    context_object_name='animal_list'
    template_name='animals/animal_results.html'
    def get_queryset(self):
        query=self.request.GET.get('q')
        return Animal.objects.filter(
            Q(breed__icontains=query)
        )



   