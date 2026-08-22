from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('create/', views.patient_create, name='patient_create'),
    path('list/', views.patient_list, name='patient_list'),
    path('update/<int:pk>/', views.patient_update, name='patient_update'),
    path('delete/<int:pk>/', views.patient_delete, name='patient_delete'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]