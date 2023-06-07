from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.


def breg(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken!')
                return redirect('breg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Address Already in use!')
                return redirect('breg')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                user.save()
                messages.info(request, 'User Created Successfully')
                return redirect('login')

        else:
            messages.info(request, 'Password Not Matching .. ')
            return redirect('breg')

    else:
        return render(request, 'buyer.html')


def vreg(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken!')
                return redirect('vreg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Address Already in use!')
                return redirect('vreg')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                user.save()
                messages.info(request, 'User Created Successfully')
                return redirect('login')

        else:
            messages.info(request, 'Password Not Matching .. ')
            return redirect('vreg')

    else:
        return render(request, 'vendor.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Login Failed, Invalid Cridentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")
