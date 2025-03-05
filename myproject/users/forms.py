# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User  # Use this if you haven't set up CustomUser
from .models import UserProfile


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User  # Change to CustomUser if you're using a custom user model
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash password
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # Add email field
    profile_image = forms.ImageField(required=False)  # Add image field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.user:
            self.fields['email'].initial = self.instance.user.email  # Pre-fill email field

    def save(self, commit=True):
        user = self.instance.user
        user.email = self.cleaned_data['email']  # Update email
        # user.profile_image = self.cleaned_data['profile_image']  # Update Image
        if commit:
            user.save()
            if self.cleaned_data.get("profile_image"):  # Only update if a new image is uploaded
                self.instance.profile_image = self.cleaned_data["profile_image"]
            # self.instance.profile_image = self.cleaned_data.get("profile_image", self.instance.profile_image)
            self.instance.save()
        return self.instance

    class Meta:
        model = UserProfile
        fields = ['full_name', 'email','profile_image', 'company', 'job_title', 'country', 'address', 'phone', 'about']
        widgets = {
            'about': forms.Textarea(attrs={
                'rows': 5,
                'cols': 50,
                'placeholder': 'Tell us about yourself...',
                'class': 'form-control',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',  # This applies Bootstrap styling
                'placeholder': 'Email',
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',  # This applies Bootstrap styling
                'placeholder': 'Enter your full name',
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',  # This applies Bootstrap styling
                'placeholder': 'Enter your company name',
            }),
            'job_title': forms.TextInput(attrs={
                'class': 'form-control',  # This applies Bootstrap styling
                'placeholder': 'Enter your Job Title',
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',  # This applies Bootstrap styling
                'placeholder': 'Country',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',  # This applies Bootstrap styling
                'placeholder': 'Address',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',  # This applies Bootstrap styling
                'placeholder': 'Phone',
            }),

        }


# class UserRegistrationForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    # full_name = forms.CharField(max_length=255)
    # company = forms.CharField(max_length=255, required=False)
    # job = forms.CharField(max_length=255, required=False)
    # country = forms.CharField(max_length=100, required=False)
    # address = forms.CharField(widget=forms.Textarea, required=False)
    # phone = forms.CharField(max_length=20, required=False)

    # class Meta:
        # model = User
        # fields = ['username', 'email', 'password1', 'password2', 'full_name', 'company', 'job', 'country', 'address', 'phone']

    # def save(self, commit=True):
        # user = super().save(commit=False)
        # user.email = self.cleaned_data['email']
        # if commit:
            # user.save()
            # UserProfile.objects.create(
                # user=user,
                # full_name=self.cleaned_data['full_name'],
                # company=self.cleaned_data['company'],
                # job=self.cleaned_data['job'],
                # country=self.cleaned_data['country'],
                # address=self.cleaned_data['address'],
                # phone=self.cleaned_data['phone']
            # )
        # return user
