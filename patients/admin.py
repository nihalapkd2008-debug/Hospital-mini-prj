from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'phone', 'disease')
    search_fields = ('name', 'phone')
    list_filter = ('disease',)
    list_per_page = 10

admin.site.register(Patient, PatientAdmin)