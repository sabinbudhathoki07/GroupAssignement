from django.contrib import messages
from django.shortcuts import redirect
from Tender.models import USER
from django.db.models import Q

class Authenticate:
    def valid_user(function):
        def wrap(request):
            try:
                USER.objects.get(Q(Email=request.session['Email']),Q(Password=request.session['Password']))
                return function(request)
            except:
                messages.warning(request, "Please Enter valid email or password.")
                return redirect("/login")
        return wrap

    def valid_user_include_id(function): 
        def wrap(request,id):
            try:
                USER.objects.get(Email=request.session['Email'], Password = request.session['Password'])
                return function (request,id)
            except:
                return redirect('/login')
        return wrap