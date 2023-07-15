from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from home.forms import SignUpForm

def home(request):
    '''View function for home page of site.'''
    return render(request, "index.html")

def teams(request):
    '''View function for teams page of site.'''
    return render(request, "team.html")

def login(request):
    '''View function for login page of site.'''
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
