from django.db import models
from users.models import User
from catogery.models import Catogery
class Project(models.Model):
    title = models.CharField(max_length=50,primary_key=True)
    details = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Catogery = models.ForeignKey(Catogery)
    target = models.IntegerField()
    current = models.IntegerField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()


class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')

class Tag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)



class Rate(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('project', 'user')

   