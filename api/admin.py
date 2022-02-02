from django.contrib import admin
from .models import Category,Profile, Task
# Register your models here.

admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Task)
