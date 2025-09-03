from django.contrib import admin
from .models import PTPRApplication,COVApplication,CLOApplication,ChainsawRegistration,TreeCuttingApplication,TreeCuttingPublicApplication,PrivateLandTimberPermit,SLUPApplication,FLAGApplication,LumberDealerApplication,SeedlingRequest,WPPPermit
from django.utils.html import format_html
from django.db import models



# forestry/admin.py
from django.contrib import admin
from kiosk.models import Feedback,ForestryFeedback

class ForestryFeedbackAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(app_name="forestry")

admin.site.register(ForestryFeedback, ForestryFeedbackAdmin)



@admin.register(PTPRApplication)
class PTPRApplicationAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'date_submitted')
    search_fields = ('fullname',)

@admin.register(COVApplication)
class COVApplicationAdmin(admin.ModelAdmin):
    list_display = ('reference_no', 'fullname', 'species', 'volume_cubic', 'status', 'date_submitted')
    search_fields = ('fullname', 'species', 'reference_no')
    list_filter = ('status', 'date_submitted')
    readonly_fields = ('reference_no', 'date_submitted')


@admin.register(CLOApplication)
class CLOApplicationAdmin(admin.ModelAdmin):
    list_display = ('reference_no', 'fullname', 'species', 'volume_cubic', 'destination', 'status', 'date_submitted')
    search_fields = ('fullname', 'species', 'destination', 'reference_no')
    list_filter = ('status', 'date_submitted')
    readonly_fields = ('reference_no', 'date_submitted')



@admin.register(ChainsawRegistration)
class ChainsawRegistrationAdmin(admin.ModelAdmin):
    list_display = ('reference_no', 'fullname', 'status', 'remarks', 'date_submitted')
    search_fields = ('fullname', 'reference_no')
    list_filter = ('status', 'date_submitted')
    readonly_fields = ('reference_no', 'date_submitted')



@admin.register(TreeCuttingApplication)
class TreeCuttingApplicationAdmin(admin.ModelAdmin):
    list_display = ('reference_no', 'fullname', 'plantation', 'species', 'status', 'date_submitted')
    search_fields = ('fullname', 'reference_no', 'species', 'plantation')
    list_filter = ('status', 'date_submitted')
    readonly_fields = ('reference_no', 'date_submitted')

@admin.register(TreeCuttingPublicApplication)
class TreeCuttingPublicAdmin(admin.ModelAdmin):
    list_display = ('reference_no', 'fullname', 'plantation', 'species', 'volume', 'status', 'date_submitted')
    search_fields = ('fullname', 'reference_no', 'species', 'plantation')
    list_filter = ('status', 'date_submitted')
    readonly_fields = ('reference_no', 'date_submitted')

@admin.register(PrivateLandTimberPermit)
class PrivateLandTimberPermitAdmin(admin.ModelAdmin):
    list_display = ('reference_no', 'fullname', 'lot_location', 'tree_type', 'volume', 'status', 'date_submitted')
    search_fields = ('fullname', 'reference_no', 'tree_type', 'lot_location')
    list_filter = ('status', 'date_submitted')
    readonly_fields = ('reference_no', 'date_submitted')


@admin.register(SLUPApplication)
class SLUPApplicationAdmin(admin.ModelAdmin):
    list_display = ('reference_no', 'fullname', 'location', 'project', 'status', 'date_submitted')
    search_fields = ('fullname', 'reference_no', 'project', 'location')
    list_filter = ('status', 'date_submitted')
    readonly_fields = ('reference_no', 'date_submitted')


@admin.register(FLAGApplication)
class FLAGApplicationAdmin(admin.ModelAdmin):
    list_display = ('reference_no', 'fullname', 'project_type', 'location', 'status', 'date_submitted')
    search_fields = ('fullname', 'reference_no', 'project_type', 'location')
    list_filter = ('status', 'date_submitted')
    readonly_fields = ('reference_no', 'date_submitted')


@admin.register(LumberDealerApplication)
class LumberDealerAdmin(admin.ModelAdmin):
    list_display = ('reference_no', 'fullname', 'plantation', 'species', 'volume', 'status', 'date_submitted')
    search_fields = ('fullname', 'reference_no', 'plantation', 'species')
    list_filter = ('status', 'date_submitted')
    readonly_fields = ('reference_no', 'date_submitted')




@admin.register(SeedlingRequest)
class SeedlingRequestAdmin(admin.ModelAdmin):
    list_display = ('reference_no', 'fullname', 'species', 'quantity', 'status', 'date_submitted')
    search_fields = ('fullname', 'reference_no', 'species')
    list_filter = ('status', 'date_submitted')
    readonly_fields = ('reference_no', 'date_submitted')




@admin.register(WPPPermit)
class WPPPermitAdmin(admin.ModelAdmin):
    list_display = ('reference_no', 'applicant', 'location', 'capacity', 'status', 'date_submitted')
    search_fields = ('reference_no', 'applicant', 'location')
    list_filter = ('status', 'date_submitted')
    readonly_fields = ('reference_no', 'date_submitted')






