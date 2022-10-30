from django.urls import path
from interface_module_app import views

urlpatterns = [
    path('learning_interface/', views.learning_interface, name='Learning_interface'),
    path('learning_options_panel/', views.learning_options_panel, name='Learning_options_panel'),
]