from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    # FORESTRY AREA
    path('', views.external, name='external'),
    path('sale_of_bidding_documents/', views.sale, name='sale'),



    
    
    
    
    
    
    
    
    






]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)