from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import requests
from requests import get
from .models import Profile
import zipcodes




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account is created. Please login')
            return redirect('login')
    else:
        form = UserRegisterForm
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST': 
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
   
   
    
    
    location = request.user.profile.location


    if location is None:
        final_location ="Please Enter Your Zipcode -->"
    else:   
        zipcode = request.user.profile.location
        user_location = zipcodes.matching('{}'.format(zipcode))
        city = user_location[0]['city']
        state = user_location[0]['state']
        final_location = city + ',' + ' ' + state
    
    
    
    

    context = {
        'u_form' : u_form,
        'p_form' : p_form ,
        'final_location' : final_location  
    }
    return render(request, 'users/profile.html', context)