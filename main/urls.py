from django.urls import path

from main.views import *

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("service/", show_service, name="show_service"),
    path("service/add/", create_service, name="create_service"),
    path("api/service/", get_service_json, name="get_service_json"),
    path("service/<uuid:service_id>/delete/",delete_service, name="delete_service"),
    path("service/<uuid:service_id>/edit/", edit_service, name="edit_service"),
]