from django.db import models
from users.models import User
from catogery.models import Catogery
class Project(models.Model):
    title = models.CharField(max_length=50,primary_key=True)
    details = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Catogery = models.ForeignKey(Catogery)
    target = models.IntegerField()
    current = models.IntegerField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()


class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')

class comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class tag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class reply(models.Model):
    comment = models.ForeignKey(comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class reportproject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class reportcomment(models.Model):
    comment = models.ForeignKey(comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    