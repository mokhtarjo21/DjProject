from django.shortcuts import render

def home(request):
    return render(request, 'basic.html')
# Create your views here.
