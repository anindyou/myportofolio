from django.shortcuts import render

from main.models import *


def show_main(request):
    context = {
        "name": "Anindya Raihani Hassan",
        "npm": "2506553295",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Hello, I'm Anindya Raihani Hassan. Computer Science "
            "student at Universitas Indonesia who combines UI/UX design and "
            "front-end development to turn raw ideas into clean, functional, and "
            "fully shipped projects."
        ),
        "short_info" : "Computer Science @ Universitas Indonesia",
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Anindya Raihani Hassan",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_service(request):
    context = {
        "service_list" : Service.objects.all()
    }
    return render(request, "service.html", context)