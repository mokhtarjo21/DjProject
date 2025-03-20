from django.db import models
from projects.models import Project
from users.models import User
from commentes.models import Comment





class reportproject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class reportcomment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
# Create your models here.
