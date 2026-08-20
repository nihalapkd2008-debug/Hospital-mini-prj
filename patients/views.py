from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from patients.models import Patient, Profile
from doctors.models import Doctor
from appointments.models import Appointment, ContactMessage


# ========== HOME ==========
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
    # Correct path pointing to your new home page
    return render(request, 'home.html', context)


# ========== PATIENT - CREATE ==========
def patient_create(request):
    if request.method == 'POST':
        Patient.objects.create(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            phone=request.POST.get('phone'),
            disease=request.POST.get('disease')
        )
        messages.success(request, 'Patient added successfully!')
        return redirect('patient_list')

    return render(request, 'patients/create.html')


# ========== PATIENT - READ ==========
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/list.html', {'patients': patients})


# ========== PATIENT - UPDATE ==========
def patient_update(request, pk):
    patient = get_object_or_404(Patient, id=pk)

    if request.method == 'POST':
        patient.name = request.POST.get('name')
        patient.age = request.POST.get('age')
        patient.phone = request.POST.get('phone')
        patient.disease = request.POST.get('disease')
        patient.save()

        messages.success(request, 'Patient updated successfully!')
        return redirect('patient_list')

    return render(request, 'patients/update.html', {'patient': patient})


# ========== PATIENT - DELETE ==========
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, id=pk)

    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient deleted successfully!')
        return redirect('patient_list')

    return render(request, 'patients/delete.html', {'patient': patient})


# ========== PROFILE ==========
@login_required
def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Create a profile if it doesn't exist
        profile = Profile.objects.create(
            user=request.user,
            bio="No bio provided yet.",
            phone="Not specified"
        )
        messages.info(request, 'Profile created successfully!')
    
    context = {
        'profile': profile,
    }
    return render(request, 'patients/profile.html', context)


# ========== ABOUT ==========
def about(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    context = {
        'total_doctors': doctors.count(),
        'total_patients': patients.count(),
    }

    # FIXED: Added 'patients/' path so Django can find your about.html
    return render(request, 'about.html', context)

# ========== CONTACT ==========
def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'contact.html')


def treatment_queries(request):
    patients = Patient.objects.prefetch_related('treatments')

    for patient in patients:
        list(patient.treatments.all())

    return HttpResponse("Treatment query test completed")