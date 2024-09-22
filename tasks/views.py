from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserRegistrationForm

# Create your views here.

def login_view(request):
    pass 

@login_required
def logout_view(request):
    pass


def register_view(request):
    if request.method == 'POST':
        form =  CustomUserRegistrationForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            return HttpResponse('user created')
        else:
            print('invalid form',form.errors)
    form = CustomUserRegistrationForm()
        
    return render(request,'register.html',{'form':form})