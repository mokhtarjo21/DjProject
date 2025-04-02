from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    facebook_acount = models.CharField(max_length=50, null=True)
    Birthdate = models.DateTimeField()
    phone = models.CharField(max_length=50)
    active_email = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='users/', default='default.jpg')
# Create your models here.
