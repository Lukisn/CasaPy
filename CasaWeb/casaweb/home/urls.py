from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path("", views.home_view, name="index"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("issue/", views.issue_view, name="issue"),
]
