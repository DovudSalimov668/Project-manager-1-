from django.db import models
from django.contrib.auth.models import User 





###################################

class Project(models.Model):
    user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    title_project = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    due_date = models.DateField(null=True)
    priority = models.PositiveBigIntegerField(default=1)
    created_at = models.DateField(auto_now=True)
    is_done = models.BooleanField(default=False)

    # def __str__(self):
    #     return f"{self.user} {self.title_project} ({self.description}) {self.due_date} {self.priority}  {self.created_at} {self.is_done} "     
    def __str__(self):
        return f"{self.title_project}"
    
    def show_user(self):
        return ",".join([str(p) for p in self.user.all()])    
    

class Task(models.Model):
    user = models.ForeignKey(to = User , on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title_task = models.CharField(max_length=30,unique=True)
    description = models.TextField()
    priority = models.PositiveBigIntegerField(default=1)
    due_date = models.DateField(null=True)
    created_at = models.DateField(auto_now=True)
    is_done = models.BooleanField(default=False)

 
    def __str__(self):
        return f"{self.project} {self.title_task}"  

    def get_absolute_url(self):
        return "/tasks/%i/" % self.id

