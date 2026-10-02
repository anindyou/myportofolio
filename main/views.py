from django.shortcuts import render

from main.models import *
from main.forms import *

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required

from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
import datetime

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from django.views.decorators.http import require_POST
def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No login session / Cookie not found')
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
        "last_login": last_login
    }
    return render(request, "index.html", context)

# ====================================== Experience ======================================

def show_experience(request):
    title_query = request.GET.get("title", "").strip() 
        
    context = {
        "name": "Anindya Raihani Hassan",
        "heading" : "Where I've Been",
        "caption" : "A few things I've worked on and learned from along the way.",
        "title_query": title_query,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all().order_by("-started_at")

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    data = []
    for e in experience:
        data.append({
            "pk": str(e.id),
            "fields": {
                "title": e.title,
                "institution": e.institution,
                "description": e.description,
                "started_at": e.started_at.strftime("%Y-%m-%d"),
                "ended_at": e.ended_at.strftime("%Y-%m-%d") if e.ended_at else None,
                "is_ongoing": e.is_ongoing,
            }
        })

    return JsonResponse(data, safe=False)


@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only owner can add experience."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "New experience added successfully!", "pk": str(experience.id)},
            status=201,
        )
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
    

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience added successfully!")
        return redirect("main:show_experience")

    context = {
        "name": "Anindya Raihani Hassan",
        "form": form,
        "is_edit": False,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Successfully deleted experience!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

@login_required(login_url="/login/")
@permission_required('main.change_experience', raise_exception=True)
def edit_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience successfully updated!")
        return redirect("main:show_experience")

    context = {
        "name": "Anindya Raihani Hassan",
        "form": form,
        "is_edit": True,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)  

# ====================================== Service ======================================

def show_service(request):
    title_query = request.GET.get("title", "").strip() 
    
    context = {
        "name" : "Anindya Raihani Hassan",
        "heading" : "What I bring to the table",
        "caption" : "A mix of skills I've picked up, from crafting interfaces to writing the code behind them.",
        "title_query": title_query,
        "form": ServiceForm(),
    }
    return render(request, "service.html", context)

@require_POST
def create_service_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only owner can add service."},
            status=403,
        )

    form = ServiceForm(request.POST)
    if form.is_valid():
        service = form.save()
        return JsonResponse(
            {"message": "New service added successfully!", "pk": str(service.id)},
            status=201,
        )
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
    
@login_required(login_url="/login/")
def create_service(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ServiceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New service added successfully!")
        return redirect("main:show_service")

    context = {
        "name": "Anindya Raihani Hassan",
        "form": form,
        "is_edit": False,
    }
    return render(request, "service_form.html", context)

@login_required(login_url="/login/")
def delete_service(request, service_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    service = get_object_or_404(Service, pk=service_id)

    if request.method == "POST":
        service.delete()
        messages.success(request, "Successfully deleted service!")
        return redirect("main:show_service")

    return redirect("main:show_service")

def get_service_json(request):
    title_query = request.GET.get("title", "").strip()
    service = Service.objects.prefetch_related('starred_by').all()

    if title_query:
        service = service.filter(title__icontains=title_query)

    data = []
    for s in service:
        starred_users = s.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(s.id),
            "fields": {
                "title": s.title,
                "description": s.description,
                "icon": s.icon,
                "star_count": len(starred_users),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
@permission_required('main.change_service', raise_exception=True)
def edit_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    form = ServiceForm(request.POST or None, instance=service)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Service successfully updated!")
        return redirect("main:show_service")

    context = {
        "name": "Anindya Raihani Hassan",
        "form": form,
        "is_edit": True,
        "service": service,
    }
    return render(request, "service_form.html", context)    

@login_required(login_url="/login/")
def toggle_star(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    if request.method == "POST":
        if request.user in service.starred_by.all():
            service.starred_by.remove(request.user)
        else:
            service.starred_by.add(request.user)

    return redirect("main:show_service")



# ====================================== Authentication ======================================
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("main:login")

    context = {
        "name": "Anindya Raihani Hassan",
        "form" : form,
    }

    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Anindya Raihani Hassan",
        "form": form,
    }

    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response