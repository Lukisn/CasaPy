from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home_view(request):
    return render(request, "home/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home:index")
        else:
            # TODO: flash message
            # https://docs.djangoproject.com/en/4.1/ref/contrib/messages/
            print("INVALID LOGIN!!!")
    return render(request, "home/login.html")


def logout_view(request):
    logout(request)
    return redirect("home:index")


def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            user = User.objects.create_user(username, password=password1)
            print(user)
            login(request, user)
            return redirect("home:index")
        else:
            # TODO: flash message
            print("PASSWORDS MUST MATCH!")
    return render(request, "home/signup.html")
