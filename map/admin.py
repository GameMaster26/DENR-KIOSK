from django.contrib import admin
from kiosk.models import MapFeedback
# Register your models here.







class MapFeedbackAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(app_name="map")

admin.site.register(MapFeedback, MapFeedbackAdmin)