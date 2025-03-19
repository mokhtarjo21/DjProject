from django.db import models

class Catogery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,primary_key=True)
    description = models.TextField()

# Create your models here.
