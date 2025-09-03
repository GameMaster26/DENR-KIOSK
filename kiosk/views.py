
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def homepage(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")  # balik sa homepage pagkatapos magsubmit
    else:
        form = FeedbackForm()

    return render(request, "home.html", {"form": form})


def overview(request):
    return render(request,'overview/index.html')