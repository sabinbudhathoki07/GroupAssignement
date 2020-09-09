from django.shortcuts import render, redirect
from Tender.forms import userform, postform, applyform
from Tender.models import USER, POST, APPLY
from django.contrib import messages
from Tender.authenticate import Authenticate
from django.db.models import Q
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    if request.method == "POST":
        form = userform(request.POST, request.FILES)
        form.save()
        return redirect('/login')
    form = userform()
    return render(request, 'signup.html', {'form': form})

def tender(request):
    posts = POST.objects.all()
    return render(request, "tender.html",{'posts':posts})

def aboutus(request):
    return render(request, "aboutus.html")

def faq(request):
    return render(request, "faqs.html")

def entry(request):
    try:
        request.session['Email'] = request.POST["Email"]
        request.session['Password'] = request.POST["Password"]
        user = USER.objects.get(Q(Email = request.POST['Email']) & Q(Password = request.POST['Password']))
        request.session['user_id'] = user.id
        return redirect("/dashboard")
    except:
        messages.warning(request, "invalid username/password")
        return redirect('/login')
        
@Authenticate.valid_user
def dashboard(request):
    posts = POST.objects.raw("select * from post_data where user_id = %s", [request.session['user_id']])
    user = USER.objects.get(id=request.session['user_id'])
    return render(request, 'dashboard.html', {'posts': posts,'user':user})

@Authenticate.valid_user_include_id
def moreinformation(request, id):
    post =POST.objects.get(id=id)
    apply_form=applyform()
    return render(request, "moreinformation.html",{'post':post,'apply_form':apply_form})

@Authenticate.valid_user
def apply(request):
    if request.method == 'POST':
        if not request.POST._mutable:
            request.POST._mutable = True
        request.POST['user']=request.session['user_id']
        apply =applyform(request.POST)
        apply.save()
    return redirect('/')

@Authenticate.valid_user
def upload(request):
    if request.method == "POST":
        if not request.POST._mutable:
            request.POST._mutable = True
        request.POST['user']=request.session['user_id']
        post_form = postform(request.POST, request.FILES)
        post_form.save()
        return redirect('/upload')
    else:
       post_form = postform()    
    return render(request, 'upload.html',{'post_form':post_form} )

@Authenticate.valid_user_include_id
def post_edit(request, id):
    posts = POST.objects.get(id=id)
    return render(request, "post_edit.html",{'posts':posts})

@Authenticate.valid_user_include_id
def post_update(request, id):
    posts = POST.objects.get(id=id)
    if not request.POST._mutable:  
        request.POST._mutable = True
    request.POST['user'] = request.session['user_id']
    form = postform(request.POST,request.FILES, instance=posts)
    form.save()
    return redirect('/dashboard')

@Authenticate.valid_user_include_id
def post_delete(request, id):
    POST.objects.get(id=id).Tender_Image.delete()
    post = POST.objects.get(id=id)
    post.delete()
    return redirect('/dashboard')

@Authenticate.valid_user_include_id
def account_edit(request,id):
    users = USER.objects.get(id=id)
    return render(request, "edit_user.html",{'users':users})

@Authenticate.valid_user_include_id
def update_user(request, id):
    user = USER.objects.get(id=id)
    if not request.POST._mutable:  
        request.POST._mutable = True
    U_form = userform(request.POST,request.FILES, instance=user)
    U_form.save()
    return redirect('/dashboard')

@Authenticate.valid_user_include_id
def user_delete(request, id):
    USER.objects.get(id=id).image.delete()
    user = USER.objects.get(id=id)
    user.delete()
    return redirect('/')

@Authenticate.valid_user_include_id
def application(request, id):
    applicants = APPLY.objects.raw("Select * from apply_data where post_id = %s" ,[id])
    return render(request, "application.html",{'applicants':applicants})

def logout(request):
    del request.session['Email']
    del request.session['Password']
    del request.session['user_id']
    return redirect("/")