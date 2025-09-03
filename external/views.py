from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.

#EXTERNAL AREA
def external(request):
    return render(request, 'kiosk/external/external.html')


def sale(request):
    return render(request, 'kiosk/external/sale.html')



