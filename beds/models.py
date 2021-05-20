from django.db import models
from django.contrib.auth.models import User
# Create your models here.
dt=(
('AL', 'ALAPPUZHA'),
('ER', 'ERNAKULAM'),
('ID', 'IDUKKI'),
('KN', 'KANNUR'),
('KS', 'KASARGOD'),
('KL', 'KOLLAM'),
('KT', 'KOTTAYAM'),
('KZ', 'KOZHIKODE'),
('MA', 'MALAPPURAM'),
('PL', 'PALAKKAD'),
('PT','PATHANAMTHITTA'),
('TV','TRIVANDRUM'),
('TS', 'THRISSUR'),
('WA', 'WAYANAD')
)
class Hospital(models.Model):
    sc=(
    ('GV', 'GOVERNMENT'),
    ('PR', 'PRIVATE')
    )
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    district=models.CharField(max_length=2, choices=dt)
    phone=models.CharField(max_length=20)
    sector=models.CharField(max_length=2, choices=sc)
    covid_beds=models.CharField(max_length=20)
    normal_beds=models.CharField(max_length=20)
    icu_beds=models.CharField(max_length=20)
    ventilator=models.CharField(max_length=20)
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Patient(models.Model):
    ca=(
    ('CV', 'COVID'),
    ('NC', 'NON-COVID')
    )
    st=(
    ('WT', 'WAITING'),
    ('AD', 'ADMITTED'),
    ('DS', 'DISCHARGED')
    )
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    aadhar=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    location=models.CharField(max_length=50)
    district=models.CharField(max_length=2, choices=dt)
    category=models.CharField(max_length=2, choices=ca)
    status=models.CharField(max_length=2, choices=st, blank=True, default='WT')

    def __str__(self):
        return self.name

class BedAllocation(models.Model):
    ct=(
    ('C', 'COVID'),
    ('N', 'NORMAL'),
    ('I', 'ICU'),
    ('V', 'VENTILATOR')
    )
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital=models.ForeignKey(Hospital, on_delete=models.CASCADE)
    category=models.CharField(max_length=2, choices=ct)
