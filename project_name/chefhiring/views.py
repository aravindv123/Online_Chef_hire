from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import *
from .forms import UserRegistrationForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Signup successful! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'chefhiring/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home1')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'chefhiring/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

def home(request):
    return render(request, 'chefhiring/home.html')

def home1(request):
    return render(request, 'chefhiring/home1.html')

def userhome(request):
    return render(request, 'chefhiring/userhome.html')

def chef_view(request):
    return render(request, 'chefhiring/chef_view.html')

def complete_view(request):
    return render(request, 'chefhiring/CompleteRegistration.html')

def chef_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chef_view')
            else:
                messages.error(request, 'Invalid username or password.')
    return render(request, 'chefhiring/Chef_login.html', {'form': form})

def userlogin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('userhome')
            else:
                messages.error(request, 'Invalid username or password.')
    return render(request, 'chefhiring/login.html', {'form': form})

# Corrected chef_signup function
def chef_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # Check if passwords match
        if password != password_confirm:
            messages.error(request, "Passwords do not match!")
            return redirect('chef_signup')

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('chef_signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('chef_signup')

        # Create the User and Chef records
        user = User.objects.create(username=username, email=email, password=make_password(password))
        # Chef.objects.create(username=username, email=email, password=make_password(password))
        chef = Chef(
            username=username,
            email=email,
            password=make_password(password)
        )
        chef.save()

        messages.success(request, "Chef registered successfully!")
        return redirect('login')  # Redirect to login page after successful signup
    else:
        return render(request, 'chefhiring/Chef_signup.html')
