from django.shortcuts import render


# Create your views here.

def home(request):
    '''View function for home page of site.'''
    return render(request, "index.html")


def teams(request):
    '''View function for teams page of site.'''
    return render(request, "team.html")


def login(request):
    '''View function for login page of site.'''
    return render(request, "login.html")


def signup(request):
    '''View function for register page of site.'''
    return render(request, "signup.html")
