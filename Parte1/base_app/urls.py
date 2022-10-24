from django.urls import path
from base_app import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('login/', views.login, name='Login'),
    path('sign_up/', views.sign_up, name='Sign_up'),
    path('learning_interface/', views.learning_interface, name='Learning_interface '),
    path('learning_mastering/', views.learning_mixture, name='Learning_mixture'),
    path('learning_mixture/', views.learning_mastering, name='Learning_mastering'),
    path('tips/', views.tips, name='Tips'),
    path('evaluations/', views.evaluations, name='Evaluations'),
    path('who_we_are/', views.who_we_are, name='Who_we_are'),
    path('about/', views.about, name='About'),
    path('feedback/', views.feedback, name='Feedback'),
]