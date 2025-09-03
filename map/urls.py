from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # MAP AREA
    path('', views.map, name='map'),
    path('land_use/', views.landUse, name='landUse'),
    path('forest_management/', views.forestManagement, name='forestManagement'),
    path('protected_areas/', views.protectedAreas, name='protectedAreas'),
    path('mining_zone/', views.miningZone, name='miningZone'),
    path('gis_services/', views.gisServices, name='gisServices'),
    path('hazard_risk/', views.hazardRisk, name='hazardRisk'),


    
    
    
    
    
    
    
    
    






]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)