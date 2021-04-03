from api.models import ProjectForm
from api.serializers import ProjectSerializer
from rest_framework import generics
from django.shortcuts import render

# Create your views here.

class ProjectList(generics.ListCreateAPIView):
    queryset = ProjectForm.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectForm.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'unit_status'

def index(request):
    return render(request,'index.html')
