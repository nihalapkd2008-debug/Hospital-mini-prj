from django.shortcuts import render, redirect
from django.contrib import messages
from appointments.models import Appointment
from patients.models import Patient
from doctors.models import Doctor

def appointment_list(request):
    appointments = Appointment.objects.all()
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    
    context = {
        'appointments': appointments,
        'patients': patients,
        'doctors': doctors,
    }
    return render(request, 'appointments/list.html', context)

def book_appointment(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        reason = request.POST.get('reason')
        status = request.POST.get('status', 'Pending')
        
        patient = Patient.objects.get(id=patient_id)
        doctor = Doctor.objects.get(id=doctor_id)
        
        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            date=date,
            time=time,
            reason=reason,
            status=status
        )
        messages.success(request, 'Appointment booked successfully!')
        return redirect('appointment_list')
    
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'appointments/book.html', {
        'patients': patients,
        'doctors': doctors
    })