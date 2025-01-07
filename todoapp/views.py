from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if username exists
        if not User.objects.filter(username=username).exists():
            messages.warning(request, "Username not found.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('home')
        else:
            messages.warning(request, "Invalid credentials. Please try again.")
            return redirect('login')

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        agreement = request.POST.get('agreement')

        # Check if passwords match
        if pass1 != pass2:
            messages.warning(request, "Passwords do not match!")
            return redirect('signup')

        # Check if the agreement checkbox is checked
        if not agreement:  # If agreement is not checked, this will be empty
            messages.warning(request, "You must agree to the terms and conditions!")
            return redirect('signup')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username already exists!")
            return redirect('signup')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email is already registered!")
            return redirect('signup')

        try:
            # Create and save the new user
            user = User.objects.create_user(username=username, email=email, password=pass1)
            user.save()
            messages.success(request, "Successfully Signed Up! Please log in.")
            return redirect('login')  # Redirect to login page after successful signup
        except Exception as e:
            messages.warning(request, "Something went wrong. Please try again later.")
            return redirect('signup')

    return render(request, 'signup.html')

def recovery(request):
    return render(request, 'recovery.html')

def terms(request):
    return render(request, 'terms.html')
def home(request):
    return render(request,'home.html')
def logout(request):
        auth_logout(request)
        messages.success(request, "Successfully logged out!")
        return redirect('login') 
