from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Doctor, Department


# ========== DOCTOR LIST ==========

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/list.html', {
        'doctors': doctors
    })


# ========== DOCTOR CREATE ==========

def doctor_create(request):
    departments = Department.objects.all()

    if request.method == 'POST':
        department_id = request.POST.get('department')

        Doctor.objects.create(
            name=request.POST.get('name'),
            specialization=request.POST.get('specialization'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            department_id=department_id
        )

        messages.success(request, 'Doctor added successfully!')
        return redirect('doctor_list')

    return render(request, 'doctors/create.html', {
        'departments': departments
    })


# ========== DOCTOR UPDATE ==========

def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, id=pk)
    departments = Department.objects.all()

    if request.method == 'POST':
        doctor.name = request.POST.get('name')
        doctor.specialization = request.POST.get('specialization')
        doctor.phone = request.POST.get('phone')
        doctor.email = request.POST.get('email')

        department_id = request.POST.get('department')
        doctor.department = Department.objects.get(id=department_id)

        doctor.save()

        messages.success(request, 'Doctor updated successfully!')
        return redirect('doctor_list')

    return render(request, 'doctors/update.html', {
        'doctor': doctor,
        'departments': departments
    })


# ========== DOCTOR DELETE ==========

def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, id=pk)

    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'Doctor deleted successfully!')
        return redirect('doctor_list')

    return render(request, 'doctors/delete.html', {
        'doctor': doctor
    })