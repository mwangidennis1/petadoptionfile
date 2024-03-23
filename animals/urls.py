from django.urls import path
from .views import AnimalListView,AnimalDetailView,AnimalAdoptView,adopt_me_view,SearchResultListView
from . import views

urlpatterns=[
    path('',AnimalListView.as_view(),name='animal_list'),
    path('<uuid:pk>',AnimalDetailView.as_view(),name='animal_detail'),
    path('adopt/<uuid:animal_id>',AnimalAdoptView.as_view(),name='animal_adopt'),
    path('adoptus/',views.adopt_me_view,name='adopt_us'),
    
    path('search/',SearchResultListView.as_view(),name='search_results')
]