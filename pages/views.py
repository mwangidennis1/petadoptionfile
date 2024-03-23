from django.views.generic import TemplateView
from django.shortcuts import render,get_object_or_404,redirect
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name='about.html'
class SuccessView(TemplateView):
    template_name='animals/success_form.html'

def testing(request):
    return redirect('/animals')
  