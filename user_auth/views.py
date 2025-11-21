from django.shortcuts import render, redirect
from user_auth.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
# Registration page
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = RegisterForm()
    return render(request, 'user_auth/register.html', {'form': form})


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
            return render(request, 'user_auth/login.html', {
                'error': 'Invalid username or password',
                'next': next_url
            })

    # GET request
    return render(request, 'user_auth/login.html', {'next': next_url})

# Logout
def user_logout(request):
    logout(request)
    return redirect('login')