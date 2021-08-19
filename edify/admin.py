from django.contrib import admin
from .models import Mathamatics
from .models import Physics
from .models import Chemistry
from .models import Contact
# Register your models here.
admin.site.register(Mathamatics)
admin.site.register(Physics)
admin.site.register(Chemistry)
admin.site.register(Contact)
