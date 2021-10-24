from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def home(request):

    post = Post.objects.all()
    return render(request,"User/home.html",{'post':post})


def login(request):

    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['pwd']
        
        user = auth.authenticate(username=uname,password=password)
     

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request,"User/login.html")



def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']

        if pwd1 == pwd2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email is Already Exist")
                return redirect('register')
            else:
                u = User.objects.create(first_name=fname,last_name=lname,username=uname,email=email)
                u.set_password(pwd1)
                u.save()
                messages.info(request,f"Thanks for Signin {uname}")
                return redirect('login')

        else:
            messages.info(request,"Passord 1 should be match to password 2")
            return redirect('register')

    return render(request,"User/register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def newPost(request,pk):
    
    if request.method == 'POST':
        newdata = request.POST['data']
        title = request.POST['title']
        print(newdata)
        user = User.objects.filter(username=pk)
        print(user)
        for i in user: 
            p = Post.objects.create(user=i,text=newdata,title=title)
            p.save()

       
        return redirect('/')
    return render(request,"User/newpost.html")