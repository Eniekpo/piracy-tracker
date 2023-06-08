from django.shortcuts import render
from . forms import VendorForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'admin.html')


def vendor(request):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Sign Up Successfully')
        return HttpResponseRedirect('login')
    context = {'form': form}

    return render(request, 'vendor.html', context)


def buyer(request):
    return render(request, 'buyer.html')
