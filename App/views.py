from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'admin.html')


def vendor(request):
    return render(request, 'vendor.html')


def buyer(request):
    return render(request, 'buyer.html')
