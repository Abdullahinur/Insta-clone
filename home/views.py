from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Image, Profile
from .forms import SignUpForm


# Create your views here.

# View function to display the homepage
def home(request):
    home = "This is My Instagram clone"
    image = Image.get_all_images()
    return render(request, 'home/home.html', {"home": home, "image": image})


# View function to display the user login page
def user_login(request):

    return render(request, 'Userlogin/login.html')


# View function to display the dashboard after login
def dashboard(request):

    return render(request, 'dashboard/dashboard.html')


# View function to display user signup posted_images
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
