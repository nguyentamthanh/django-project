from django.shortcuts import render
from .models import Email


def home(request):
    email = {
        "title": "Calendar Invitation",
        "description": "Calendar Invitation",
        "time": "10:00",
    }
    return render(request, "home.html", {"email": email})


def detail_email(request, id):
    email = Email.objects.get(id=id)
    return render(request, "detail_email.html", {"email": email})
