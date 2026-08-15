from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from patients import views


admin.site.site_header = "Aurea Clinic Admin Panel"
admin.site.site_title = "Aurea Clinic"
admin.site.index_title = "Welcome to Aurea Clinic Administration"


urlpatterns = [
    path('admin/', admin.site.urls),

    # Main patients pages
    path('', include('patients.urls')),

    # Profile
    path('profile/', views.profile_view, name='profile'),

    # Other apps
    path('patients/', include('patients.urls')),
    path('doctors/', include('doctors.urls')),
    path('appointments/', include('appointments.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )