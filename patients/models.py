from django.db import models


class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    disease = models.TextField()

    treatments = models.ManyToManyField(Treatment, blank=True)

    def __str__(self):
        return self.name


class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.patient} - {self.date}"