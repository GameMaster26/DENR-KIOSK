from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    # InExternal AREA
    path('', views.inExternal, name='inExternal'),
    path('cert_no_records/', views.noRecords, name='noRecords'),
    path('authentication_of_records/', views.authentication, name='authentication'),
    path('payment_of_claims/', views.payment, name='payment'),


    
    
    
    
    
    
    
    
    






]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)