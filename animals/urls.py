from django.urls import path
from .views import AnimalListView,AnimalDetailView

urlpatterns=[
    path('',AnimalListView.as_view(),name='animal_list'),
    path('<uuid:pk>',AnimalDetailView.as_view(),name='animal_detail')
]