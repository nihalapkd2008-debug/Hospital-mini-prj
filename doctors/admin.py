from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'phone', 'email')
    search_fields = ('name', 'specialization')
    list_filter = ('specialization',)

admin.site.register(Doctor, DoctorAdmin)