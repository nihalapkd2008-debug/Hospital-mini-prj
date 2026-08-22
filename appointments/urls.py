from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('update/<int:pk>/', views.appointment_update, name='appointment_update'),
    path('delete/<int:pk>/', views.appointment_delete, name='appointment_delete'),

    # Day 3: Show all patients of a specific doctor
    path(
        'doctor/<int:doctor_id>/patients/',
        views.doctor_patients,
        name='doctor_patients'
    ),
]