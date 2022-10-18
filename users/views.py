from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Profile
# Create your views here.

@login_required
def user(request):
    return render(request, 'users/profile.html', {})
    
def logout_view(request):
    logout(request)
    messages.success(request, f'Usted se ha cerrado sesión')
    return redirect('transcrip:index') 



def register(request):
    if request.method == 'POST': 
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            #profile = Profile(user=User.objects.get(username= form.cleaned_data.get('username') ), location='')
            #profile.save()marcomarcomarcomarco
            messages.success(request, f'Bienvenido {username} su cuenta a sido registrada')
            return redirect('users:login')        
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})