from django.urls import path
from main import api_views

app_name = "api"
urlpatterns = [
    path("services/", api_views.services_list, name="service-list"),
    path("services/<uuid:service_id>/", api_views.service_detail, name="service-detail"),
    path("services/<uuid:service_id>/star/", api_views.service_star, name="service-star"),
]