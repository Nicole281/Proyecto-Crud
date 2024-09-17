# main/urls.py
from django.urls import path
from . import views  # Import views from the current package

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.register, name='register'),  # Use views.register
]
