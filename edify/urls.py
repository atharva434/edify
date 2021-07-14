from django.contrib import admin
from django.urls import path,include
from edify import views

admin.site.site_header ="Edify teachers panel"
admin.site.index_title ="Edify teachers panel"

urlpatterns = [
    path('',views.index ,name='index'),
    path("maths",views.courses,name='maths'),
    path("chemistry",views.chemistry,name='chemistry'),
    
    
    
]