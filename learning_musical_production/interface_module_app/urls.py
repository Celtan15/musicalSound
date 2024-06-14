from django.urls import path
from interface_module_app import views

urlpatterns = [
    path('learning_interface/', views.learning_interface, name='Learning_interface'),
    path('learning_options_panel/', views.learning_options_panel, name='Learning_options_panel'),
    path('learning_side_panel/', views.learning_side_panel, name='Learning_side_panel'),
    path('learning_top_panel/', views.learning_top_panel, name='Learning_top_panel'),
    path('learning_workstation/', views.learning_workstation, name='Learning_workstation'),
]