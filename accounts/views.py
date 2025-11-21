from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Home page
def home(request):
    return render(request, 'accounts/home.html')
# Welcome page (requires login)
@login_required
def welcome(request):
    return render(request, 'accounts/welcome.html', {'user': request.user})



