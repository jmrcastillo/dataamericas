# from django.shortcuts import render

# # Create your views here.
# users/views.py
from rest_framework import views
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .forms import UserRegistrationForm, UserLoginForm
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.response import Response
from .models import UserProfile
from rest_framework import serializers, views, status

import logging

logger = logging.getLogger(__name__)  # Set up logger


def register_view(request):    # This was missing
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            logger.info("✅ Form is valid")  # Logs output
            user = form.save()

            # Create an empty UserProfile associated with this user
            UserProfile.objects.create(user=user)

            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            logger.error("❌ Form errors: %s", form.errors)  # Logs errors
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/pagesregister.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                logger.info("✅ Form is valid")  # Logs output
                return redirect('home')
        logger.error("❌ Form errors: %s", form.errors)  # Logs errors
        messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'users/pageslogin.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    logger.info(request, 'You have been logged out.')
    return redirect('login')

@login_required
def user_profile_view(request):
    # user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_profile = request.user.userprofile

    if request.method == 'POST':
        print("POST Data:", request.POST)  # Debugging step
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'users/profile.html', {'form': form,
                                                  'email': request.user.email,
                                                  'profile': user_profile})

@login_required
def upload_profile_image(request):
    if request.method == 'POST':
        form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
    return redirect('profile')

@login_required
def delete_profile_image(request):
    profile = request.user.profile
    profile.delete_image()
    return redirect('profile')

# @login_required
# def user_profile_view(request):
    # print("User:", request.user, "Authenticated:", request.user.is_authenticated)

    # try:
        # user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        # print(f"UserProfile {'created' if created else 'fetched'}:", user_profile)
    # except Exception as e:
        # print("Error fetching/creating UserProfile:", e)
        # user_profile = None

    # if request.method == 'POST':
        # print("Test Post")
        # form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        # if form.is_valid():
            # print("Cleaned Data:", form.cleaned_data)  # Debugging
            # form.save()
            # messages.success(request, "Profile updated successfully!")
            # print("Profile saved successfully!")  # Confirm saving
            # return redirect('user_profile')
        # else:
            # print("Form errors:", form.errors)  # Debugging
    # else:
        # form = UserProfileForm(instance=user_profile)

    # return render(request, 'users/profile.html', {'form': form, 'profile': user_profile})
