import socket

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import pyrebase


# Create your views here.
class main:
    firebaseConfig = {
        'apiKey': "AIzaSyCYNkErgR4_fpfbHJAO_KKxjYH8KRzIT7g",
        'authDomain': "story-84a74.firebaseapp.com",
        'databaseURL': "https://story-84a74.firebaseio.com",
        'projectId': "story-84a74",
        'storageBucket': "story-84a74.appspot.com",
        'messagingSenderId': "841980057493",
        'appId': "1:841980057493:web:50118f53b187aafcf8089c"
    };
    firebase = pyrebase.initialize_app(firebaseConfig);
    dbase = firebase.database()
    storage = firebase.storage()

    def index(request):
        ipv4 = socket.gethostbyname(socket.gethostname())
        address = socket.gethostbyaddr(ipv4)
        soctype = socket.socketpair()
        storiesData= main.dbase.child("StoriesDetails").shallow().get().val()
        list=[];
        print(storiesData);
        if storiesData is not None:
            for i in storiesData:
                print(i);
                list.append(main.dbase.child("StoriesDetails").child(i).get().val())
        if 'UsersEmails' in request.session:
            print(request.session['UsersEmails'])

            savedCookie = request.session['UsersEmails']


            return render(request, 'index.html', {'title': 'titles', 'cal': 'cal','ips':[ipv4,address,soctype],'cookiesName':savedCookie,'storiesData':list})
        return render(request, 'index.html', {'title': 'titles', 'cal': 'cal','ips':[ipv4,address,soctype],'cookiesName':None,'storiesData':list})


