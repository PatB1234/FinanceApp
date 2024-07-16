# Django imports
from django.template import loader
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# DB Interaction imports
from .forms import *
from .databse import *


def index(request):

    try:

        if request.session['loginStatus'] == "False":

            print("Need to login")
            request.session['code'] = 2
            return render(request, "financeapp/login.html")
        else:

            return render(request, "financeapp/index.html")
    except:
        request.session['code'] = 2
        print("Need to login")
        return render(request, "financeapp/login.html")


def login(request):

    # Validate that the user logging in actually exists within the program database
    if request.method == "POST":

        form = UserLogin(request.POST)
        if form.is_valid():

            loginData = form.cleaned_data
            isLoginDataValid = loginCheck(
                loginData['email'], loginData['password'])
            print(isLoginDataValid)
            if isLoginDataValid == True:

                request.session['loginStatus'] = "True"
                request.session['uid'] = getUserIDByEmail(loginData['email'])
                request.session['code'] = 1
                return HttpResponseRedirect("/FinanceApp/")
            else:
                request.session['loginStatus'] = "False"
                request.session['code'] = 3
                return HttpResponseRedirect("/FinanceApp/login")

    else:
        form = UserLogin()
        return render(request, "financeapp/login.html")


def signUp(request):

    if request.method == "POST":

        # Create a new user
        form = UserSignUp(request.POST)
        if form.is_valid():

            data = form.cleaned_data
            createUser(name=data['name'], email=data['email'],
                       password=data['password'])
            request.session['loginStatus'] = "True"
            request.session['uid'] = getUserIDByEmail(data['email'])
            request.session['code'] = 1
            return HttpResponseRedirect("/FinanceApp/")

        else:

            print('A problem occured during user creation')
            request.session['loginStatus'] = "False"
            request.session['code'] = 2
            return HttpResponseRedirect("/FinanceApp/")

    else:

        form = UserSignUp()
        return render(request, "financeapp/signup.html")
