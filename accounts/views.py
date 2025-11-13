from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login



def home(request):
    return render(request, 'accounts/home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'accounts/welcome.html', {'user': user})
        else:
            return render(request, 'accounts/login.html', {'error': 'invalid username or password'})
        
    return render(request, 'accounts/login.html')
        

                

