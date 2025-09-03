from django.urls import path
from . import views

app_name = 'biodiversity'

urlpatterns = [
    path('', views.biodiversity, name='biodiversity'),  # ✅ This handles /biodiversity/
    path('wildlife-registration/', views.wildlife_registration, name='wildlife_registration'),
    path('wildlife-farm-permit/', views.wildlife_farm_permit, name='wildlife_farm_permit'),
    path('local-transport-permit/', views.local_transport_permit, name='local_transport_permit'),
    path('gratuitous-permit/', views.gratuitous_permit, name='gratuitous_permit'),
    path('special-local-transport-permit/', views.special_local_transport_permit, name='special_local_transport_permit'),
    path('marine-research-clearance/', views.marine_research_clearance, name='marine_research_clearance'),
]
