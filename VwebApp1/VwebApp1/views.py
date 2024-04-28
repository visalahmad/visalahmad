# It containe views function.
# each view function should have a parameter as request

from django.http import HttpResponse

def Home(request):
    return HttpResponse("<h1 style='background-color:red;'>Welcome to home page!!!</h1>")

def About(request):
    return HttpResponse("<h1>Welcome to About page!!!</h1>")

def Contact(request):
    return HttpResponse("<h1>Welcome to Contact page!!!</h1>")

def Services(request):
    return HttpResponse("<h1>Welcome to Services page!!! <a href='/Home'>Home</a></h1>")