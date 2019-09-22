import socket

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
class main:

    def index(request):
        ipv4 = socket.gethostbyname(socket.gethostname())
        address = socket.gethostbyaddr(ipv4)
        soctype = socket.socketpair()

        return render(request, 'index.html', {'title': 'titles', 'cal': 'cal','ips':[ipv4,address,soctype]})


