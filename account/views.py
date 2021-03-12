from django.contrib.auth import login
from django.shortcuts import render, redirect, HttpResponse

from .forms import MyUserCreationForm


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