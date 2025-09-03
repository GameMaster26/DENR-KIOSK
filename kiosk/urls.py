from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name = "kiosk"

urlpatterns = [
    path('', views.index, name='indexx'),
    path('feedback', views.homepage, name='homepage'),


    
    
    
    
    
    
    
    
    






]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)