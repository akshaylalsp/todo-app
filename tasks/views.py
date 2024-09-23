from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserRegistrationForm,TaskCreateForm,LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login,authenticate
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return HttpResponse('logined')
        else:
            
            return HttpResponse('error')
    form = LoginForm()
    return render(request,'login.html',{'form':form})


@login_required
def logout_view(request):
    return redirect('login')



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

@login_required
def add_task_view(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user=request.user
            task.save()
            return HttpResponse('task added')
        else:
            pass
    form = TaskCreateForm()
    return render(request,'add_task.html',{'form':form})
