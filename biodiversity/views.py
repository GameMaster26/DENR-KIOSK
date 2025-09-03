# biodiversity/views.py
from django.shortcuts import render, redirect
from .forms import WildlifeRegistrationForm,WildlifeFarmPermitForm,LocalTransportPermitForm,GratuitousPermitMOAForm,SpecialLocalTransportPermitForm,MarineResearchClearanceForm
from .models import WildlifeRegistration,WildlifeFarmPermit,LocalTransportPermit,GratuitousPermitMOA,SpecialLocalTransportPermit,MarineResearchClearance

# Create your views here.
#BIODIVERSITY AREA
def biodiversity(request):
    return render(request, 'kiosk/biodiversity/biodiversity.html')

def wildlife_registration(request):
    if request.method == 'POST':
        form = WildlifeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('biodiversity:wildlife_registration')
    else:
        form = WildlifeRegistrationForm()

    registrations = WildlifeRegistration.objects.all().order_by('-date_submitted')

    context = {
        'form': form,
        'registrations': registrations,
    }
    return render(request, 'kiosk/biodiversity/wildlife_registration.html', context)

def wildlife_farm_permit(request):
    if request.method == 'POST':
        form = WildlifeFarmPermitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('biodiversity:wildlife_farm_permit')
    else:
        form = WildlifeFarmPermitForm()

    permits = WildlifeFarmPermit.objects.all().order_by('-date_submitted')

    context = {
        'form': form,
        'permits': permits,
    }
    return render(request, 'kiosk/biodiversity/wildlife_farm_permit.html', context)

def local_transport_permit(request):
    if request.method == 'POST':
        form = LocalTransportPermitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('biodiversity:local_transport_permit')
    else:
        form = LocalTransportPermitForm()

    permits = LocalTransportPermit.objects.all().order_by('-date_submitted')

    context = {
        'form': form,
        'permits': permits,
    }
    return render(request, 'kiosk/biodiversity/local_transport_permit.html', context)

def gratuitous_permit(request):
    if request.method == 'POST':
        form = GratuitousPermitMOAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('biodiversity:gratuitous_permit')
    else:
        form = GratuitousPermitMOAForm()

    requests_list = GratuitousPermitMOA.objects.all().order_by('-date_submitted')
    return render(request, 'kiosk/biodiversity/gratuitous_permit.html', {
        'form': form,
        'requests_list': requests_list
    })


def special_local_transport_permit(request):
    if request.method == 'POST':
        form = SpecialLocalTransportPermitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('biodiversity:special_local_transport_permit')
    else:
        form = SpecialLocalTransportPermitForm()

    permits = SpecialLocalTransportPermit.objects.all().order_by('-date_submitted')

    context = {
        'form': form,
        'permits': permits,
    }
    return render(request, 'kiosk/biodiversity/special_local_transport_permit.html', context)

def marine_research_clearance(request):
    if request.method == 'POST':
        form = MarineResearchClearanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('biodiversity:marine_research_clearance')
    else:
        form = MarineResearchClearanceForm()

    clearances = MarineResearchClearance.objects.all().order_by('-date_submitted')

    context = {
        'form': form,
        'clearances': clearances,
    }
    return render(request, 'kiosk/biodiversity/marine_research_clearance.html', context)