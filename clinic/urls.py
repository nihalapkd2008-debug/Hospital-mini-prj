from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Aurea Clinic Admin Panel"
admin.site.site_title = "Aurea Clinic"
admin.site.index_title = "Welcome to Aurea Clinic Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('patients.urls')),
    path('patients/', include('patients.urls')),
    path('doctors/', include('doctors.urls')),
    path('appointments/', include('appointments.urls')),
]