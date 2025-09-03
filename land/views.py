from django.shortcuts import render,redirect
from .forms import LandClassificationApplicationForm,SurveyAuthorityApplicationForm,AgriculturalApplicationForm,ResidentialFreePatentApplicationForm,SurveyPlanApplicationForm
from .models import LandClassificationApplication,SurveyAuthorityApplication,AgriculturalApplication,ResidentialFreePatentApplication,SurveyPlanApplication


# Create your views here.

#LAND AREA
def land(request):
    return render(request, 'kiosk/land/land.html')

def landStatus(request):
    if request.method == 'POST':
        form = LandClassificationApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('land:landStatus')  # or your named URL
    else:
        form = LandClassificationApplicationForm()

    applications = LandClassificationApplication.objects.all().order_by('-last_updated')

    context = {
        'form': form,
        'applications': applications
    }
    return render(request, 'kiosk/land/landStatus.html', context)



def surveyAuthority(request):
    if request.method == 'POST':
        form = SurveyAuthorityApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('land:surveyAuthority')  # stay on same page after save
    else:
        form = SurveyAuthorityApplicationForm()

    applications = SurveyAuthorityApplication.objects.all().order_by('-last_updated')

    context = {
        'form': form,
        'applications': applications
    }
    return render(request, 'kiosk/land/surveyAuthority.html', context)
    



def free_patent_agricultural(request):
    if request.method == "POST":
        form = AgriculturalApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('land:free_patent_agricultural')
    else:
        form = AgriculturalApplicationForm()

    applications = AgriculturalApplication.objects.order_by('-submitted_at')

    context ={
        'form': form,
        'applications': applications
    }
    return render(request, 'kiosk/land/agricultural.html',context)




def free_patent_residential(request):
    if request.method == 'POST':
        form = ResidentialFreePatentApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('land:free_patent_residential')  # change to your URL name
    else:
        form = ResidentialFreePatentApplicationForm()

    applications = ResidentialFreePatentApplication.objects.all()

    context = {
        'form': form,
        'applications': applications
    }
    return render(request, 'kiosk/land/residential.html', context)




def survey_plan_approval(request):
    if request.method == 'POST':
        form = SurveyPlanApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('land:survey_plan_approval')
    else:
        form = SurveyPlanApplicationForm()

    applications = SurveyPlanApplication.objects.all()

    context = {
        'form': form,
        'applications': applications
    }
    return render(request, 'kiosk/land/surveyPlan.html', context)
    