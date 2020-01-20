import datetime

from django import forms
from django.core import validators
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
import datetime

# Create your views here.
# from story.story import settings
from django.urls import reverse
import story
from ..views import main
from ..hashCode import hashCode
import sys

class auth:
    sys.path.append(r"C:\Users\Muhammad\StudioProjects\Story\app\src\main\java\mainproject\mainroject\story\HashCode.java")

    mAuth = main.firebase.auth()
    userDetailSave = main.dbase.child("UserDetail")
    def index(request):

        savedCookie = request.COOKIES.get('UserEmail');
        if savedCookie is None:

            if (request.method == 'POST'):
                UserEmail = request.POST.get('email', None)
                Password = request.POST.get('password', None)
                response = HttpResponse("success")

                if UserEmail == "mnmfas@gmail.com" and Password == '12345678':
                    cookieExpires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=(1*24*60*60)),"%a, %d-%b-%Y %H:%M:%S GMT")
                    response.set_cookie('UserEmail',UserEmail,(1*24*60*60),cookieExpires,domain='http://127.0.0.1/')
                    request.session['UsersEmails'] = UserEmail
                    request.session.set_expiry(30000)
                    return HttpResponseRedirect(reverse('index'))

                return render(request, "auth.html", {})
        else:
            return HttpResponseRedirect(reverse('index'))

        return render(request, "auth.html", {})

    def signUp(self):
        default_validators = [validators.validate_slug]
        slug = forms.SlugField()
        UserEmail = self.POST.get('email', None)
        Password = self.POST.get('password', None)
        confirmPassword = self.POST.get('confirmpassword',None)
        firstName = self.POST.get('FirstName',None)
        secondName= self.POST.get('LastName',None)
        Gender = self.POST.get('Gender',None)
        createDate = datetime.datetime.now()
        birthDate =self.POST.get('birthdate',None)
        Name = firstName + secondName
        # if firstName is not None or secondName is not None:
        response = HttpResponse("success")
        user =auth.mAuth.create_user_with_email_and_password(UserEmail,hashCode.SHA1(Password))
        if user:
            data = {"email":UserEmail,"Name":Name ,"Password":hashCode.SHA1(Password),
                    "birthDate":birthDate,"Gender":Gender,"createdDate":createDate}
            auth.userDetailSave.push().set()
            cookieExpires = datetime.datetime.strftime(
            datetime.datetime.utcnow() + datetime.timedelta(seconds=(1 * 24 * 60 * 60)),
                "%a, %d-%b-%Y %H:%M:%S GMT")
            response.set_cookie('UserEmail', UserEmail, (1 * 24 * 60 * 60), cookieExpires, domain='http://127.0.0.1/')
            self.session['UsersEmails'] = UserEmail
            self.session.set_expiry(30000)
            return HttpResponseRedirect(reverse('index'))

        return render(self, "auth.html", {})

    #
    # def logout(request):
    #     try:
    #         del request.session['member_id']
    #     except KeyError:
    #         pass
    #     return HttpResponse("You're logged out.")

    # def set_cookie(response,key,value,days_expire = 7):
    #     if days_expire is None:
    #         max_age = 365 * 24 * 60 * 60
    #     else:
    #         max_age = days_expire * 24 * 60 * 60
    #
    #     expires = datetime.datetime.strftime(datetime.datetime.utcnow())
    #
