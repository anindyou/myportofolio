from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Service
from main.permissions import IsPortfolioOwnerOrReadOnly, IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import ServiceSerializer

@api_view(["GET", "HEAD", "POST"]) 
# mengubah fungsi standar python  ke DRF view handlers
# kalau request di luar fungsi tersebut, langsung direject (405 Method Not Allowed)
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def services_list(request):
    if request.method in ("GET", "HEAD"):
        services = Service.objects.prefetch_related("starred_by").order_by("title", "id")
        title = request.query_params.get("title", "").strip()
        if title:
            services = services.filter(title__icontains=title)
        serializer = ServiceSerializer(
            services, many=True, context = {"request": request},
        )
        return Response(serializer.data)

    serializer = ServiceSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def service_detail(request, service_id):
    service = get_object_or_404(
        Service.objects.prefetch_related("starred_by"), pk=service_id,
    )
    if request.method in ("GET", "HEAD"):
        serializer = ServiceSerializer(service, context = {"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ServiceSerializer(
        service, data=request.data, partial=request.method == "PATCH",
        context = {"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

# Untuk API, mengembalikan data terbaru agar frontend dapat memperbarui tampilan tanpa pindah halaman
@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def service_star(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    if service.starred_by.filter(pk=request.user.pk).exists():
        service.starred_by.remove(request.user)
    else:
        service.starred_by.add(request.user)
    serializer = ServiceSerializer(service, context = {"request": request})
    return Response(serializer.data)