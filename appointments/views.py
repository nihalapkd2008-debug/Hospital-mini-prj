from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from appointments.models import Appointment
from patients.models import Patient
from doctors.models import Doctor


# ========== APPOINTMENT LIST ==========
def appointment_list(request):
    appointments = Appointment.objects.select_related(
        'patient',
        'doctor'
    )

    # N+1 Query Problem
    for appointment in appointments:
        print(appointment.patient.name)
        print(appointment.doctor.name)

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    context = {
        'appointments': appointments,
        'patients': patients,
        'doctors': doctors,
    }

    return render(request, 'appointments/list.html', context)


# ========== BOOK APPOINTMENT ==========
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


# ========== UPDATE APPOINTMENT ==========
def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)

    if request.method == 'POST':
        appointment.patient_id = request.POST.get('patient')
        appointment.doctor_id = request.POST.get('doctor')
        appointment.date = request.POST.get('date')
        appointment.time = request.POST.get('time')
        appointment.reason = request.POST.get('reason')
        appointment.status = request.POST.get('status')

        appointment.save()

        messages.success(request, 'Appointment updated successfully!')
        return redirect('appointment_list')

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    return render(request, 'appointments/update.html', {
        'appointment': appointment,
        'patients': patients,
        'doctors': doctors
    })


# ========== DELETE APPOINTMENT ==========
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)

    if request.method == 'POST':
        appointment.delete()

        messages.success(request, 'Appointment deleted successfully!')
        return redirect('appointment_list')

    return render(request, 'appointments/delete.html', {
        'appointment': appointment
    })


# ========== DAY 3: PATIENTS OF A SPECIFIC DOCTOR ==========
def doctor_patients(request, doctor_id):
    # Step 1: Get the specific doctor
    doctor = get_object_or_404(Doctor, id=doctor_id)

    # Step 2: Find all patients who have an appointment
    # with this doctor
    patients = Patient.objects.filter(
        appointment__doctor=doctor
    ).distinct()

    # Step 3: Send doctor and patients to template
    context = {
        'doctor': doctor,
        'patients': patients,
    }

    return render(
        request,
        'appointments/doctor_patients.html',
        context
    )