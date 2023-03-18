# Create your views here.
from django.shortcuts import render, redirect
# Login required to access private pagas
from django.contrib.auth.decorators import login_required
# Prevent back button (destroy the last section)
from django.views.decorators.cache import cache_control

from . forms import DataForm, PredictionsForm

from . models import Data, Predictions

# Frontend
def frontend(request):
    return render(request, "frontend.html")


def predictions(request):
    if request.method == 'POST':
        form = PredictionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result')
    else:
        form = PredictionsForm()
    context = {
        'form': form
    }
    return render(request, "predictions.html", context)


def result(request):
    predicted_soft = Data.objects.all()
    context = {
        'predicted_soft': predicted_soft
    }
    return render(request, "result.html", context)


# Backend
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result')
    else:
        form = DataForm()
    context = {
        'form': form
    }
    return render(request, "backend.html", context)
