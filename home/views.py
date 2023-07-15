from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.forms import SignUpForm

def home(request):
    '''View function for home page of site.'''
    return render(request, "index.html")

def teams(request):
    '''View function for teams page of site.'''
    return render(request, "team.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)  # Print form errors to the console
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.main_location = request.POST.get('main_location')
        user.biography = request.POST.get('biography')
        user.interests = request.POST.get('interests')
        profile_image = request.FILES.get('profile_image')
        if profile_image:
            user.profile_image = profile_image
        user.save()
        return redirect('profile') # Redirect to profile page
    
    return render(request, 'profile.html')

@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('/')
    return render(request, 'delete_profile.html')