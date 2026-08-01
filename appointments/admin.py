from django.contrib import admin
from .models import Appointment, ContactMessage

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'status')
    search_fields = ('patient__name', 'doctor__name')
    list_filter = ('status', 'date')
    date_hierarchy = 'date'

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('created_at',)

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)