from django.contrib import admin
from django.urls import path, include
from project_task_app.views import ProjectListCreateView,ProjectDetailView,TaskDetailView, TaskListCreateView,BasePageView,user_projects,ProjectDetail,project_tasks

urlpatterns = [
   path('projects/', ProjectListCreateView.as_view()),
   path('projects/<int:pk>', ProjectDetailView.as_view()),
   path('projects/tasks', TaskListCreateView.as_view()),
   path('projects/tasks/<int:pk>', TaskDetailView.as_view()),
   path("", BasePageView.as_view() , name="base"),
   path("projects/edit/<int:pk>", ProjectDetailView.as_view(), name='project_edit'),
   path("projects/tasks/edit/<int:pk>", TaskDetailView.as_view(), name='task_edit'), 
   path('all_projects/', user_projects, name = "whole_projects"),  
   path("projects", ProjectListCreateView.as_view(), name='projects_options'),
   path("projects_detail/<int:pk>", ProjectDetail.as_view(), name="project_detail"), 
   path('projects_detail/tasks/<int:pk>', project_tasks, name = "project_tasks"),
   path("projects/tasks", TaskListCreateView.as_view(), name='task_options'),
]
