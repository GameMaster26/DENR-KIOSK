# biodiversity/admin.py
from django.contrib import admin
from .models import WildlifeFarmPermit, WildlifeRegistration,LocalTransportPermit, GratuitousPermitMOA,SpecialLocalTransportPermit,MarineResearchClearance
from kiosk.models import BiodiversityFeedback


class BiodiversityFeedbackAdmin(admin.ModelAdmin):
    list_display = ("message", "app_name", "created_at")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(app_name="biodiversity")

admin.site.register(BiodiversityFeedback, BiodiversityFeedbackAdmin)


@admin.register(WildlifeRegistration)
class WildlifeRegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'cultural_type', 'date_submitted', 'status')
    list_filter = ('cultural_type', 'status', 'date_submitted')
    search_fields = ('full_name', 'address', 'valid_id')


@admin.register(WildlifeFarmPermit)
class WildlifeFarmPermitAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'habitat_type', 'date_submitted', 'status')
    list_filter = ('habitat_type', 'status', 'date_submitted')
    search_fields = ('full_name', 'address', 'contact_number')



@admin.register(LocalTransportPermit)
class LocalTransportPermitAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'provision_type', 'date_submitted', 'status')
    list_filter = ('provision_type', 'status', 'date_submitted')
    search_fields = ('full_name', 'address', 'contact_number')


@admin.register(GratuitousPermitMOA)
class GratuitousPermitMOAAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'regulation_type', 'date_submitted')
    list_filter = ('regulation_type',)
    search_fields = ('full_name',)



@admin.register(SpecialLocalTransportPermit)
class SpecialLocalTransportPermitAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'adaptation_type', 'date_submitted', 'status')
    list_filter = ('adaptation_type', 'status', 'date_submitted')
    search_fields = ('full_name', 'address', 'contact_number')



@admin.register(MarineResearchClearance)
class MarineResearchClearanceAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'support_type', 'date_submitted', 'status')
    list_filter = ('support_type', 'status', 'date_submitted')
    search_fields = ('full_name', 'address', 'contact_number')
