from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.

#EXTERNAL AREA
def inExternal(request):
    return render(request, 'kiosk/inExternal/inExternal.html')




def noRecords(request):
    return render(request, 'kiosk/inExternal/norecords.html')




def authentication(request):
    return render(request, 'kiosk/inExternal/authentication.html')




def payment(request):
    return render(request, 'kiosk/inExternal/payment.html')





