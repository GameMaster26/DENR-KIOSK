from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from kiosk import views
urlpatterns = [
    path('admin/overview', views.overview, name='overview'),
    path('admin/', admin.site.urls),
   
    path('biodiversity/', include(('biodiversity.urls', 'biodiversity'), namespace='biodiversity')),
    path('land/', include(('land.urls', 'land'), namespace='land')),
    path('af_Internal_and_External_Services/', include(('inExternal.urls', 'inExternal'), namespace='inExternal')),
    path('af_External_Service/', include(('external.urls', 'external'), namespace='external')),
    path('forestry/', include(('forestry.urls', 'forestry'), namespace='forestry')),
    path('map/', include(('map.urls', 'map'), namespace='map')),
    path('', include(('kiosk.urls'), namespace='kiosk')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
