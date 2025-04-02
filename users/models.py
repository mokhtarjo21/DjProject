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
    def __str__(self):
        return self.fname
class user_active(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.CharField(max_length=50)
    time_send = models.DateTimeField(auto_now_add=True)
    
# Create your models here.