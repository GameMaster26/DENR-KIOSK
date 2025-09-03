from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    # FORESTRY AREA
    path('', views.forestry, name='forestry'),
    path('private_tree_plantation/', views.ptpr, name='ptpr'),
    path('cov_certificate/', views.cov, name='cov'),
    path('lumber_origin/', views.clo, name='clo'),
    path('chainsaw/', views.chainsaw, name='chainsaw'),
    path('treecutting_gov/', views.treecutting_gov, name='treecutting_gov'),
    path('treecutting_public/', views.treecutting_public, name='treecutting_public'),
    path('private_land_timber/', views.pltp, name='pltp'),
    path('slup/', views.slup, name='slup'),

    
    path('flag/', views.flag, name='flag'),
    path('lumber_dealer/', views.lumber_dealer, name='lumber_dealer'),
    path('seedling_assist/', views.seedling_assist, name='seedling_assist'),
    path('wpp_permit/', views.wpp_permit, name='wpp_permit'),

    
    
    
    
    
    
    
    
    






]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)