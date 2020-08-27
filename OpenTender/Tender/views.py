from django.shortcuts import render, redirect
from Tender.forms import userform, postform, applyform
from Tender.models import USER, POST
from django.contrib import messages
from Tender.authenticate import Authenticate

def index(request):
    return render(request, "index.html")

def notice(request):
    return render(request, "notice.html")


def login(request):
    return render(request, 'login.html')


def entry(request):
    request.session['Email'] = request.POST["Email"]
    request.session['Password'] = request.POST["Password"]
    if (request.session['Email'] == "admin@gmail.com"):
        if (request.session['Password'] == "admin"):
            return redirect('/page')
    else:
        users= USER.objects.get(Email=request.session['Email'])
        user_id = users.user_id
        return redirect("/dashboard/'" + str(user_id) + "'")

def signup(request):
    if request.method == "POST":
        form = userform(request.POST, request.FILES)
        form.save()
        return redirect('login')
    form = userform()
    return render(request, 'signup.html', {'form': form})

def tender(request):
    return render(request, "tender.html")

def aboutus(request):
    return render(request, "aboutus.html")

def faq(request):
    return render(request, "faqs.html")

def moreinformation(request):
    return render(request, "moreinformation.html")

@Authenticate.valid_user
def dashboard(request, id):
    dashboard = USER.objects.get(user_id=id)
    return render(request, 'dashboard.html', {'dashboard': dashboard})

def page(request):
    posts = POST.objects.all()
    return render(request, "page.html",{'posts':posts})
    
def upload(request):
    if request.method == 'POST':
        post_form = postform(request.POST, request.FILES)
        post_form.save()
        return redirect("/upload")
    else:
        post_form = postform()
        return render(request, 'upload.html', {'post_form': post_form})

def post_edit(request, id):
    posts = POST.objects.get(post_id=id)
    return render(request, "post_edit.html",{'posts':posts})

def post_update(request, id):
    post = POST.objects.get(post_id=id)
    post_form= postform(request.Post, request.files, instance=post)
    post_form.save
    return redirect('/page.html')

def apply(request):
    if request.method == 'POST':
        apply_form = applyform(request.POST, request.FILES)
        apply_form.save()
        return redirect("/upload")
    else:
        apply_form = applyform()
        return render(request, 'apply.html', {'apply_form': apply_form})