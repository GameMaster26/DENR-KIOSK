from django.contrib import admin
from .models import LandClassificationApplication,SurveyAuthorityApplication,AgriculturalApplication,ResidentialFreePatentApplication,SurveyPlanApplication
from kiosk.models import Feedback,LandFeedback




class LandFeedbackAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(app_name="land")

admin.site.register(LandFeedback, LandFeedbackAdmin)


@admin.register(LandClassificationApplication)
class LandClassificationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'status', 'last_updated')
    list_filter = ('status',)
    search_fields = ('full_name', 'address')



@admin.register(SurveyAuthorityApplication)
class SurveyAuthorityApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'confirmation_of_affidavit_of_adjoining_owners', 'dar_certification', 'denr_and_certification', 'technical_description', 'brgy_clearance', 'deed_of_conveyance', 'letter_request', 'sketch_plan', 'status', 'last_updated')
    list_filter = ('status', 'last_updated')
    search_fields = ('full_name', 'confirmation_of_affidavit_of_adjoining_owners', 'dar_certification', 'denr_ad_certification', 'technical_description', 'brgy_clearance', 'deed_of_conveyance', 'letter_request', 'sketch_plan')
    ordering = ('-last_updated',)



@admin.register(AgriculturalApplication)
class AgriculturalApplicationAdmin(admin.ModelAdmin):
    list_display = ('reference_no', 'owner_name', 'project_name', 'status', 'submitted_at')
    list_filter = ('status', 'construction_type')
    search_fields = ('reference_no', 'owner_name', 'project_name')


@admin.register(ResidentialFreePatentApplication)
class ResidentialFreePatentAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'proponent_name', 'status', 'last_updated')
    list_filter = ('status',)
    search_fields = ('project_name', 'proponent_name', 'project_location')



@admin.register(SurveyPlanApplication)
class SurveyPlanApplicationAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'role', 'status', 'date_submitted')
    list_filter = ('status', 'role')
    search_fields = ('fullname', 'community', 'contact')


