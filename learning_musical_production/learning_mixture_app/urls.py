from django.urls import path
from learning_mixture_app import views

urlpatterns = [
    path('learning_mixture/', views.learning_mixture, name='Learning_mixture'),
    path('learning_glossary/', views.learning_glossary, name='Learning_glossary'),
    path('learning_concepts/', views.learning_concepts, name='Learning_concepts'),
    path('learning_basic_techniques/', views.learning_basic_techniques, name='Learning_basic_techniques'),
    path('learning_mid_techniques/', views.learning_mid_techniques, name='Learning_mid_techniques'),
]