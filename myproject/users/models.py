# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from users.forms import UserRegistrationForm, UserLoginForm

# def register_view(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'Registration successful!')
#             return redirect('home')
#         else:
#             messages.error(request, 'Registration failed. Please correct the errors.')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'users/pagesregister', {'form': form})


from django.db import models

# Create your models here.
#Step 1: Create users app structure
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


# class CustomUser(AbstractUser):
    # # Add custom fields if needed
    # class Meta:
        # app_label = 'users'  # Explicitly define the app label


# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import CustomUser
from django.contrib.auth import get_user_model


# class UserRegistrationForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    # class Meta:
        # model = CustomUser
        # fields = ['username', 'email', 'password1', 'password2']

# class UserLoginForm(AuthenticationForm):
    # class Meta:
        # model = CustomUser


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django User
    full_name = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # New image field
    # about = models.CharField(max_length=255, blank=True, default="")
    about = models.TextField(blank=True, default="")
    company = models.CharField(max_length=255, blank=True, default="")
    job_title = models.CharField(max_length=255, blank=True, default="")
    country = models.CharField(max_length=100, blank=True, default="")
    address = models.CharField(max_length=100, blank=True, default="")
    phone = models.CharField(max_length=20, blank=True, default="")

    def __str__(self):
        return self.user.username


# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Valid Form")
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            print("Invalid Form")
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
                return redirect('home')
        messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'users/pageslogin.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'users/home.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

