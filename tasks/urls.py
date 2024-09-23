from django.urls import path
from .views import register_view,login_view,logout_view,add_task_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('add/',add_task_view,name='add')
]