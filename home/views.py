from django.shortcuts import render
from .models import Image


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
