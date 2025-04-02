from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings



def home(request):
    # subject = 'Hello from Django'
    # message = 'This is a test email sent from Django.'
    # recipient_list = ['mokhtar.jo21@gmail.com']
    
    # # Send the email
    # send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

    # print("Email sent successfully!")

    return render(request, 'users/active.html')
# Create your views here.
