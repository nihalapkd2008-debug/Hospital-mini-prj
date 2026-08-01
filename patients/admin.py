from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'phone', 'disease')
    search_fields = ('name', 'phone')
    list_filter = ('disease',)

admin.site.register(Patient, PatientAdmin)