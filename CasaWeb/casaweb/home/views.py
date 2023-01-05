from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import ContactForm, IssueForm


def home_view(request):
    return render(request, "home/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Login successful")
            return redirect("home:index")
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Username or Password incorrect",
                extra_tags="danger",
            )
    return render(request, "home/login.html")


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Logout successful")
    return redirect("home:index")


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            user = User.objects.create_user(username, password=password1)
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Signup successful")
            return redirect("home:index")
        else:
            messages.add_message(
                request, messages.ERROR, "Passwords must match", extra_tags="danger"
            )
    return render(request, "home/signup.html")


def about_view(request):
    return render(request, "home/about.html")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # TODO: process contact form: save to db and/or send email
            messages.add_message(
                request, messages.SUCCESS, "Thank you for getting in touch."
            )
            return redirect("home:index")
        else:
            messages.add_message(
                request, messages.ERROR, "Invalid Form", extra_tags="danger"
            )
    else:
        form = ContactForm()
    context = {"form": form}
    return render(request, "home/contact.html", context)


def issue_view(request):
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            # TODO: process issue report form
            messages.add_message(
                request, messages.SUCCESS, "Thank you for reporting the issue."
            )
            return redirect("home:index")
        else:
            messages.add_message(
                request, messages.ERROR, "Invalid Form", extra_tags="danger"
            )
    else:
        form = IssueForm()
    context = {"form": form}
    return render(request, "home/issue.html", context)
