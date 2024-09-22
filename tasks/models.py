from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11,blank=True)
    username = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Tasks(models.Model):
    user = models.ForeignKey(CustomUser,to_field='username',on_delete=models.CASCADE,related_name='user_detail')
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name