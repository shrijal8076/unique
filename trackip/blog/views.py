from django.shortcuts import render, HttpResponseRedirect
#from django.contrib.auth.forms import UserCreationForm
from . forms import SignUpForm,LogInForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group
from .signals import login_sucess
# Create your views here.
#home
def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})
#about
def about(request):
    return render(request,'about.html')
#contact
def contact(request):
    return render(request,'contact.html')
#Dashboard
def dashboard(request):


    if request.user.is_authenticated:
        Posts = Post.objects.all()
        user = request.user
        gps = user.groups.all()
        fullname = user.get_full_name()
        ip = request.session.get('ip',0)
        return render(request,'dashboard.html',{'ip':ip,'posts':Posts,'fullname':fullname,'groups':gps})
    else:
        return HttpResponseRedirect('/login')

# user login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LogInForm(request=request ,data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                passw = form.cleaned_data['password']
                user = authenticate(username=uname, password=passw)
                if user is not None:
                    messages.success(request, 'Congratulations , thank you for LogIn your self')

                    login(request, user)

                    return HttpResponseRedirect('/dashboard')
        else:
            form = LogInForm()

        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard')

#Sign up
def user_signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations , thank you for register yor self')
            user = form.save()
            group = Group.objects.get(name='author')
            user.groups.add(group)
    else:
        form = SignUpForm()

    return render(request,'signup.html' ,{'form':form})
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Add new Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title,desc=desc)
                pst.save()
                form = PostForm()
            else:
                form = PostForm()
        else:
            form = PostForm()
        return render(request,'addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login')
# Update new Post
def update_post(request ,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
            else:
                pi = Post.objects.get(pk=id)
                form = PostForm(instance=pi)
        else:
            form = PostForm()
        return render(request,'updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login')
#delete post
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login')
