from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse

from .forms import MyUserCreationForm, MyUserLogin


def register(request):
    if request.method == "POST":
        user_form = MyUserCreationForm(request.POST)
        if user_form.is_valid():
            my_user = user_form.save()
            login(request, my_user)
            return redirect('homepage')
        else:
            HttpResponse("Your form is Invalid")
    else:
        user_form = MyUserCreationForm()
    context = {
        'user_form': user_form,
    }
    return render(request, 'account/register.html', context=context)


def profile(request):
    template_name = 'account/profile.html'
    context = {

    }
    return render(request, template_name=template_name, context=context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('user_profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        my_user = authenticate(request, username=username, password=password)
        if my_user is not None:
            login(request, my_user)
            return redirect('user_profile')
        else:
            HttpResponse("Invalid Login")
    else:
        my_form = AuthenticationForm()
        context = {
            'my_form':my_form,
        }

    return render(request, 'account/login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('homepage')