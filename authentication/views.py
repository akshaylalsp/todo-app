from django.shortcuts import render,HttpResponse

# Create your views here.
def login_view(request):
    return HttpResponse("Login Page")

def logout_view(request):
    return HttpResponse("Logout Page")

def register_view(request):
    return HttpResponse("Register Page")