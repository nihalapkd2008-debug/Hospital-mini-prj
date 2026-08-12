from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('update/<int:pk>/', views.appointment_update, name='appointment_update'),
    path('delete/<int:pk>/', views.appointment_delete, name='appointment_delete'),
]