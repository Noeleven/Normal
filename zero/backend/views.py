from django.shortcuts import render
from backend.serializer import *
from rest_framework import viewsets, permissions

# Create your views here.
class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all().order_by("id")
    serializer_class = CinemaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(createUser=self.request.user)

def index(request):
    return render(request, '../frontend/index.html')
