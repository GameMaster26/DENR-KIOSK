from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import PTPRApplicationForm,COVApplicationForm,CLOApplicationForm,ChainsawRegistrationForm,TreeCuttingApplicationForm,TreeCuttingPublicForm,PrivateLandTimberPermitForm,SLUPApplicationForm,FLAGApplicationForm,LumberDealerForm,SeedlingRequestForm,WPPPermitForm
from .models import PTPRApplication,COVApplication,CLOApplication,ChainsawRegistration,TreeCuttingApplication,TreeCuttingPublicApplication,PrivateLandTimberPermit,SLUPApplication,FLAGApplication,LumberDealerApplication,SeedlingRequest,WPPPermit
# Create your views here.

#FORESTRY AREA
def forestry(request):
    return render(request, 'kiosk/forestry/forestry.html')




def ptpr(request):
    search_query = request.GET.get('search', '')

    if request.method == 'POST':
        form = PTPRApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your application has been submitted successfully!")
            return redirect('/forestry/private_tree_plantation/?tab=form')
    else:
        form = PTPRApplicationForm()

    # Filtering logic
    applications = PTPRApplication.objects.all()
    if search_query:
        applications = applications.filter(fullname__icontains=search_query)

    context = {
        'search_query': search_query,
        'form': form,
        'applications': applications,
    }

    return render(request, 'kiosk/forestry/ptpr.html', context)



def cov(request):
    if request.method == 'POST':
        form = COVApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forestry:cov')  # refresh page after submit
    else:
        form = COVApplicationForm()


    applications = COVApplication.objects.order_by('-date_submitted')

    context = {
        'form': form,
        'applications': applications
    }
    return render(request, 'kiosk/forestry/cov-certification.html',context)



def clo(request):
    if request.method == 'POST':
        form = CLOApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forestry:clo')  # namespace
    else:
        form = CLOApplicationForm()

    applications = CLOApplication.objects.order_by('-date_submitted')

    context = {
        'form': form,
        'applications': applications
    }
    return render(request, 'kiosk/forestry/lumber-origin.html',context)



def chainsaw(request):
    if request.method == 'POST':
        form = ChainsawRegistrationForm(request.POST, request.FILES)  # ✅ include FILES
        if form.is_valid():
            form.save()
            return redirect('forestry:chainsaw')
    else:
        form = ChainsawRegistrationForm()

    applications = ChainsawRegistration.objects.order_by('-date_submitted')

    context = {
        'form': form,
        'applications': applications
    }
    return render(request, 'kiosk/forestry/chainsaw-registration.html', context)




def treecutting_gov(request):
    if request.method == 'POST':
        form = TreeCuttingApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forestry:treecutting_gov')
    else:
        form = TreeCuttingApplicationForm()

    applications = TreeCuttingApplication.objects.order_by('-date_submitted')

    context = {
        'form': form,
        'applications': applications
    }
    return render(request, 'kiosk/forestry/tree-cutting.html',context)



def treecutting_public(request):
    if request.method == 'POST':
        form = TreeCuttingPublicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forestry:treecutting_public')
    else:
        form = TreeCuttingPublicForm()

    applications = TreeCuttingPublicApplication.objects.order_by('-date_submitted')

    context ={
        'form': form,
        'applications': applications
    }
    return render(request, 'kiosk/forestry/tree-cutting-public.html',context)




def pltp(request):
    if request.method == 'POST':
        form = PrivateLandTimberPermitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forestry:pltp')
    else:
        form = PrivateLandTimberPermitForm()

    applications = PrivateLandTimberPermit.objects.order_by('-date_submitted')
    context = {
        'form': form,
        'applications': applications,
    }
    return render(request, 'kiosk/forestry/pltp.html', context)




def slup(request):
    if request.method == 'POST':
        form = SLUPApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forestry:slup')
    else:
        form = SLUPApplicationForm()

    applications = SLUPApplication.objects.order_by('-date_submitted')
    context = {
        'form': form,
        'applications': applications,
    }
    return render(request, 'kiosk/forestry/slup.html', context)







def flag(request):
    if request.method == 'POST':
        form = FLAGApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forestry:flag')
    else:
        form = FLAGApplicationForm()

    applications = FLAGApplication.objects.order_by('-date_submitted')
    context = {
        'form': form,
        'applications': applications,
    }
    return render(request, 'kiosk/forestry/flag.html', context)





def lumber_dealer(request):
    if request.method == 'POST':
        form = LumberDealerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forestry:lumber_dealer')
    else:
        form = LumberDealerForm()

    applications = LumberDealerApplication.objects.order_by('-date_submitted')
    context = {
        'form': form,
        'applications': applications,
    }
    return render(request, 'kiosk/forestry/lumberDealer.html', context)




def seedling_assist(request):
    if request.method == 'POST':
        form = SeedlingRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forestry:seedling_assist')
    else:
        form = SeedlingRequestForm()

    requests = SeedlingRequest.objects.order_by('-date_submitted')
    context = {
        'form': form,
        'requests': requests,
    }
    return render(request, 'kiosk/forestry/seedling.html', context)






def wpp_permit(request):
    if request.method == 'POST':
        form = WPPPermitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forestry:wpp_permit')
    else:
        form = WPPPermitForm()

    permits = WPPPermit.objects.order_by('-date_submitted')
    context = {
        'form': form,
        'permits': permits,
    }
    return render(request, 'kiosk/forestry/wpp.html', context)
