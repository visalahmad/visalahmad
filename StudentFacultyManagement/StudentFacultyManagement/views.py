# It containe views function.
# each view function should have a parameter as request

from django.shortcuts import render

def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
   return render(request, 'contact.html')

def Services(request):
    return render(request, 'services.html')

def Test(request):
    return render(request, 'test.html')