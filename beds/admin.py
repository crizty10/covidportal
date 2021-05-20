from django.contrib import admin
from .models import Hospital,Patient,BedAllocation
# Register your models here.
admin.site.site_header= "CoviHELP"
admin.site.site_title= "CoviHELP"
admin.site.site_url= "/beds"

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    fieldsets = (
    ( None, {
        'fields': ('name', 'location', 'district', 'phone', 'sector')
    }),
    ('Bed Information', {
        'fields': ('covid_beds', 'normal_beds', 'icu_beds', 'ventilator')
    }),
    ('User Information', {
        'fields': ('user',)
    }),
    )
    list_display = ('name', 'covid_beds', 'normal_beds', 'icu_beds', 'ventilator', 'total_beds')
    list_filter = ('location', 'district', 'sector')
    radio_fields = {"sector": admin.HORIZONTAL}
    ordering = ['name']
    search_fields = ['name', 'location']

    @admin.display(description='Total Beds')
    def total_beds(self, obj):
        total_beds = int(obj.covid_beds) + int(obj.normal_beds) + int(obj.icu_beds) + int(obj.ventilator)
        return total_beds

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','location', 'category', 'status')
    list_filter = ('location', 'district')
    ordering = ['name']
    search_fields = ['name', 'location']

@admin.register(BedAllocation)
class BedAllocationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'category')
    raw_id_fields = ("patient", "hospital",)
    search_fields = ['patient__location']

    def save_model(self, request, obj, form, change):
        patient=Patient.objects.get(pk=obj.patient.id)
        patient.status='AD'
        patient.save()
        hospital=Hospital.objects.get(pk=obj.hospital.id)
        if obj.category == 'C':
            hospital.covid_beds = int(hospital.covid_beds) - 1
        if obj.category == 'N':
            hospital.normal_beds = int(hospital.normal_beds) - 1
        if obj.category == 'I':
            hospital.icu_beds = int(hospital.icu_beds) - 1
        if obj.category == 'V':
            hospital.ventilator = int(hospital.ventilator) - 1
        hospital.save()
        super().save_model(request, obj, form, change)
