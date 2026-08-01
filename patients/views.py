from django.shortcuts import render, redirect
from django.contrib import messages
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from appointments.models import ContactMessage

def home(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    appointments = Appointment.objects.all()
    
    context = {
        'patients': patients,
        'doctors': doctors,
        'appointments': appointments,
        'total_patients': patients.count(),
        'total_doctors': doctors.count(),
        'total_appointments': appointments.count(),
    }
    return render(request, 'home.html', context)

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/list.html', {'patients': patients})

def about(request):
    doctors = Doctor.objects.all()
    return render(request, 'about.html', {'total_doctors': doctors.count()})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    
    return render(request, 'contact.html')