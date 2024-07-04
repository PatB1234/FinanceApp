from django.template import loader
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.


def index(request):
    return render(request, "financeapp/index.html")


def login(request):

    return render(request, "financeapp/login.html")


def signUp(request):

    return render(request, "financeapp/signup.html")
