from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def profile_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/profile.html')

def home_view(request):
    if(request.method == 'GET'):
        return render(request, 'accounts/home.html')