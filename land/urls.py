from django.urls import path
from land import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # LAND AREA
    path('', views.land, name='land'),
    path('land_classification_status/', views.landStatus, name='landStatus'),
    path('survey_authority/', views.surveyAuthority, name='surveyAuthority'),
    path('free_patent_agricultural/', views.free_patent_agricultural, name='free_patent_agricultural'),
    path('free_patent_residential/', views.free_patent_residential, name='free_patent_residential'),
    path('survey_plan_lams_approval/', views.survey_plan_approval, name='survey_plan_approval'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)