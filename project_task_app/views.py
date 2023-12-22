from rest_framework.generics import *   
from django.views.generic import TemplateView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import  Project, Task
from apis.serializers import ProjectDetailSerializer, ProjectListCreateSerializer,TaskListCreateSerializer,TaskDetailSerializer
from apis.permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.permissions import  IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.response import Response


# Create your views here.

class ProjectListCreateView(CreateAPIView):
    # queryset = Project.objects.all().order_by("id")
    serializer_class = ProjectListCreateSerializer
    permission_classes = [IsAuthenticated,]


    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)  
    
      
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.validated_data["user"] = request.user
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
  
  



class TaskListCreateView(CreateAPIView):
    queryset = Task.objects.all().order_by("id")
    serializer_class = TaskListCreateSerializer
    permission_classes = [IsAuthenticated,]
    

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)   
 

class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [IsAuthenticated,]


class BasePageView(TemplateView):
    template_name = "main_base.html"


def user_projects(request):
  user_projects = Project.objects.filter(user = request.user.id)

  return render(request, template_name = "projects/whole_projects.html", 
                context ={"user_projects": user_projects})    


class ProjectDetail(DetailView):
    model = Project 
    template_name = "projects/project_detail.html"
    context_object_name = 'project' 


def project_tasks(request, pk):
  project_tasks = Task.objects.filter(project = pk)

  return render(request, template_name = "tasks/project_tasks.html", 
                context ={"project_tasks": project_tasks})
