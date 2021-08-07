from django.contrib import admin
from .models import Name, Task
# Register your models here.
admin.site.register(Task)
admin.site.register(Name)