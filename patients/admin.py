from django.contrib import admin
from .models import Patient, MedicalRecord, Treatment, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'bio')
    
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'phone',
        'disease',
        'show_treatments'
    )
    search_fields = ('name', 'phone')
    list_filter = ('disease',)
    list_per_page = 10

    def show_treatments(self, obj):
        return ", ".join(
            treatment.name
            for treatment in obj.treatments.all()
        )

    show_treatments.short_description = 'Treatments'