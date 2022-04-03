from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
# Create your views here.
# from story.story import settings
from django.urls import reverse
import story
from ..views import main
from ..hashCode import hashCode
import sys
import json

class auth:

    mAuth = main.firebase.auth()
    userDetailSave = main.dbase.child("UserDetail")
    def index(request):

        savedcookie = request.COOKIES.get('UserEmail');
        if savedcookie is None:

            if request.method == 'POST':
                user_email = request.POST.get('email', None)
                password = request.POST.get('password', None)
                response = HttpResponse("success")

                if user_email == "mnmfas@gmail.com" and password == '12345678':
                    cookie_expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=(1*24*60*60)), "%a, %d-%b-%Y %H:%M:%S GMT")
                    response.set_cookie('UserEmail', user_email, (1*24*60*60), cookie_expires, domain='http://127.0.0.1/')
                    request.session['UsersEmails'] = user_email
                    request.session.set_expiry(30000)
                    return HttpResponseRedirect(reverse('index'))

                return render(request, "auth.html", {})
        else:
            return HttpResponseRedirect(reverse('index'))

        return render(request, "auth.html", {})

    def signup(self):
        # default_validators = [validators.validate_slug]
        # slug = forms.SlugField()
        errors = auth.validate_request(self.POST)
        # print(self.POST)
        if errors:
            print(errors)
            return;
        useremail = self.POST.get('email', None)
        password = self.POST.get('password', None)
        username = self.POST.get('UserName' ,None)
        confirmpassword = self.POST.get('confirmpassword' ,None)
        firstname = self.POST.get('FirstName' ,None)
        secondname = self.POST.get('LastName' ,None)
        gender = self.POST.get('Gender' ,None)
        createdate = datetime.datetime.now()
        birthdate = self.POST.get('birthdate', None)
        policies = self.POST.get('privaciesAndPolicies', None)
        disclaimer = self.POST.get('disclaimer', None)
        name = firstname + " " + secondname
        # if firstName is not None or secondName is not None:
        response = HttpResponse("success")
        if policies and disclaimer:
            user = auth.mAuth.create_user_with_email_and_password(useremail, hashCode.SHA1(password))
            if user:
                data = {"email": useremail, "Name": name, "Password": hashCode.SHA1(password), "disclaimerchecked": disclaimer,
                        "policiesAndTermsChecked": policies,
                        "birthDate": birthdate, "Gender": gender, "createdDate": str(createdate), "storageUserSize": 0,
                        "maxUserStorageSize": 1024}
                # json.dump(data,default=self.datetime_handler)
                auth.userDetailSave.child(username).set(data)
                cookieexpires = datetime.datetime.strftime(
                    datetime.datetime.utcnow() + datetime.timedelta(seconds=(1 * 24 * 60 * 60)),
                    "%a, %d-%b-%Y %H:%M:%S GMT")
                response.set_cookie('UserEmail', useremail, (1 * 24 * 60 * 60), cookieexpires,
                                    domain='https://127.0.0.1/')
                self.session['UsersEmails'] = useremail
                self.session.set_expiry(30000)
                return HttpResponseRedirect(reverse('index'))
        # render(self, "auth.html", {})
        return HttpResponseRedirect(reverse('auth'))

    @staticmethod
    def validate_request(data):
        # print(data)
        errors = {}

        # dar(data);
        for i in data:
            if "required|" in data[i]:
                if auth.required(data[i]):
                    errors[i] = "{} is required".format(i)
                    print(i)
            if "same:" in data[i]:
                if not auth.same(i, ""):
                    errors[i] = "{} must match ".format(i)
        return errors;

    @staticmethod
    def same(item1, item2):
        return item1 == item2

    @staticmethod
    def required(item):
        return item is None or item == '';

    def terms(self):
        return render(self, "termsAndcoditions.html", {})

    @staticmethod
    def subtract(value):
        place = value.find("same")
        if place > -1:
            if "|" in value[place:]:
                oRplace = value[place:].find("|")
                lastVal = value[place:oRplace]
                return lastVal
            else:
                lastVal = value[place:]
                return lastVal

        return "passed Data Value"

    def logout(self):
        response = HttpResponseRedirect(reverse('index'))
        response.delete_cookie('UserEmail')
        self.session['UsersEmails'] = None
        return response

    def datetime_handler(x):
        if isinstance(x, datetime.datetime):
            return x.isoformat()
        raise TypeError("Unknown type")

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
