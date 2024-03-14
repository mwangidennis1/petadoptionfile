from django.urls import path
from .views import AnimalListView,AnimalDetailView,AnimalAdoptView

urlpatterns=[
    path('',AnimalListView.as_view(),name='animal_list'),
    path('<uuid:pk>',AnimalDetailView.as_view(),name='animal_detail'),
    path('adopt/',AnimalAdoptView.as_view(),name='animal_adopt')
]