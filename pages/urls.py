from django.urls import path
from .views import HomePageView,AboutPageView,SuccessView,testing
from . import views

urlpatterns = [
#path('', HomePageView.as_view(), name='home'),
path('about/',AboutPageView.as_view(),name='about'),
path('success_form/',SuccessView.as_view(),name='success'),
path('',views.testing,name='testing')
]
