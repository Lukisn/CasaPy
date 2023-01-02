from django.shortcuts import render
from .models import Entry


def blog(request):
    entries = Entry.objects.all()
    context = {"entries": entries}
    return render(request, "blog/index.html", context)


def details(request, pk):
    entry = Entry.objects.get(id=pk)
    comments = entry.comments.all()
    context = {"entry": entry, "comments": comments}
    return render(request, "blog/details.html", context)


def create(request):
    return render(request, "blog/create.html")
