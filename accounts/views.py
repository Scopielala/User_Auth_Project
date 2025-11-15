from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Home page
def home(request):
    return render(request, 'accounts/home.html')


# Registration page
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


# Login page
def user_login(request):
    next_url = request.GET.get('next', 'welcome')  # Default redirect after login

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next', 'welcome')  # Preserve next if POST

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(next_url)  # Redirect to next page or welcome
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password',
                'next': next_url
            })

    # GET request
    return render(request, 'accounts/login.html', {'next': next_url})


# Welcome page (requires login)
@login_required
def welcome(request):
    return render(request, 'accounts/welcome.html', {'user': request.user})


# Logout
def user_logout(request):
    logout(request)
    return redirect('login')
