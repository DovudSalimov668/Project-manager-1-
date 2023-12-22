from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User 
from project_task_app.models import  Project, Task
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import redirect
from django.urls import reverse_lazy
class ProjectListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ('user',)

    
class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ('user',)
        
    

class TaskListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = 'project','title_task','description','due_date','is_done','user',

    
class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"   

