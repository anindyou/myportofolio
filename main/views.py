from django.shortcuts import render

from main.models import *
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import *

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
        "heading" : "Where I've Been",
        "caption" : "A few things I've worked on and learned from along the way.",
    }
    return render(request, "experience.html", context)

def show_service(request):
    json_response = get_service_json(request)

    services = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    services = [service.object for service in services]
    title_query = request.GET.get("title", "").strip() 
    
    context = {
        "name" : "Anindya Raihani Hassan",
        "service_list" : services,
        "heading" : "What I bring to the table",
        "caption" : "A mix of skills I've picked up, from crafting interfaces to writing the code behind them.",
        "title_query": title_query,
    }
    return render(request, "service.html", context)

def create_service(request):
    form = ServiceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New service successfully added!")
        return redirect("main:show_service")

    context = {
        "name": "Anin",
        "form": form,
    }
    return render(request, "service_form.html", context)

def delete_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    if request.method == "POST":
        service.delete()
        messages.success(request, "Successfully deleted service!")
        return redirect("main:show_service")

    return redirect("main:show_service")

def get_service_json(request):
    title_query = request.GET.get("title", "").strip()
    service = Service.objects.all()

    if title_query:
        service = service.filter(title__icontains=title_query)

    service_json = serializers.serialize("json", service)
    return HttpResponse(service_json, content_type="application/json")