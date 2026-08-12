from django.contrib import admin
from .models import Doctor, Department

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'phone', 'email')
    search_fields = ('name', 'specialization')
    list_filter = ('specialization',)
    list_per_page = 10

admin.site.register(Doctor)
admin.site.register(Department)