from django.shortcuts import render

# Create your views here.



#MAP AREA
def map(request):
    return render(request, 'kiosk/map/map.html')

def landUse(request):
    return render(request, 'kiosk/map/land-use.html')

def forestManagement(request):
    return render(request, 'kiosk/map/forest-management.html')

def protectedAreas(request):
    return render(request, 'kiosk/map/protected-areas.html')

def miningZone(request):
    return render(request, 'kiosk/map/mining-zones.html')

def gisServices(request):
    return render(request, 'kiosk/map/gis-services.html')

def hazardRisk(request):
    return render(request, 'kiosk/map/hazard-risk.html')



