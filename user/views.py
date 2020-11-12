from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages

#TODO: User Authentication System

def userRegister(request):
    ''' Creating User Registration Form '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'{username} your Account is Created!!!')
            return redirect('login')
    #Form
    form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'user/register.html', context)

def userLogin(request):
    ''' User Authenticate for Login Purpose '''
    if request.method == 'POST':
        user = User.objects.get(username=request.POST['username'])
        if user.password == request.POST['password']:
            request.session['username'] = user.username
            messages.success(request, f'{user.username} You have Successfully Logged In!')
            return redirect('homepage')
        else:
            print('incorrect')
    #Form
    form = UserLoginForm()

    context = {'form': form}
    return render(request, 'user/login.html', context)