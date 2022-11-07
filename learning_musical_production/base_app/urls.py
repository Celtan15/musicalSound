from django.urls import include, path
from base_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='Home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='Login'),
    path('logout/', LogoutView.as_view(template_name=''), name='Logout'),
    path('sign_up/', views.sign_up, name='Sign_up'),
    path('index/', views.index, name='Index'),
    path('learning_mastering/', views.learning_mixture, name='Learning_mixture'),
    path('learning_mixture/', views.learning_mastering, name='Learning_mastering'),
    path('tips/', views.tips, name='Tips'),
    path('evaluations/', views.evaluations, name='Evaluations'),
    path('who_we_are/', views.who_we_are, name='Who_we_are'),
    path('about/', views.about, name='About'),
    path('feedback/', views.feedback, name='Feedback'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)