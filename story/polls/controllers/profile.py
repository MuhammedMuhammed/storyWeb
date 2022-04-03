import socket

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
class profile:

    def index(request):

        return render(request, "profile.html", {});