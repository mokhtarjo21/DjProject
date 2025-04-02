from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.views import View
class login(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        current_password = User.objects.get(email=email).password
        if password == current_password:
            # Send email
            subject = 'Login Successful'
            message = 'You have successfully logged in.'
            request.session['id']=User.objects.get(email=email).id
            request.session['fname']=User.objects.get(email=email).fname
            login(request)
            return render(request, 'home.html')
        else:
            return render(request, 'users/login.html')

class register(View):
    def get(self, request):
        return render(request, 'users/signup.html')

    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        facebook_acount = request.POST.get('facebook_acount')
        Birthdate = request.POST.get('Birthdate')
        phone = request.POST.get('phone')
        # user = User(fname=fname, lname=lname, email=email, password=password, facebook_acount=facebook_acount, Birthdate=Birthdate, phone=phone)
        # user.save()
        # subject = 'Welcome to Our Service'
        # message = f'Hello {fname}, thank you for registering!'
        # send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
        return render(request, 'user/activation.html')