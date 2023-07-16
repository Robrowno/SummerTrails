from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.forms import SignUpForm, UploadImageForm
from authentication.models import PhotoImage

def home(request):
    images = PhotoImage.objects.all()
    context = {'images': images}
    return render(request, "index.html", context)

def teams(request):
    '''View function for teams page of site.'''
    return render(request, "team.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}! Please login.")
            return redirect('login')
        else:
            messages.error(request, "Invalid form data.")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
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

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('home')
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form})