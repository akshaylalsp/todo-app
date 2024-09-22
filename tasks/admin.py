from django.contrib import admin
from .models import CustomUser,Tasks
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Tasks)
