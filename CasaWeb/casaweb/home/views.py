from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def home_view(request):
    return render(request, "home/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("home:index")
        else:
            # Return an 'invalid login' error message.
            print("INVALID LOGIN!!!")
    return render(request, "home/login.html")


def logout_view(request):
    logout(request)
    return redirect("home:index")


def signup_view(request):
    return render(request, "home/signup.html")
