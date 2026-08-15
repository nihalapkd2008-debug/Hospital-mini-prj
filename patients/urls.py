from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    # Patient CRUD
    path('treatment-queries/', views.treatment_queries, name='treatment_queries'),
    path('list/', views.patient_list, name='patient_list'),
    path('create/', views.patient_create, name='patient_create'),
    path('update/<int:pk>/', views.patient_update, name='patient_update'),
    path('delete/<int:pk>/', views.patient_delete, name='patient_delete'),

    # Profile
    path('profile/', views.profile_view, name='profile'),

    # Other pages
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]