from django.shortcuts import render,HttpResponse
from .models import Chemistry, Contact, Physics,phyimg,chemimg,Mathamatics,mathimg
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# Create your views here.
def index(request):

    
    return render(request,'loll.html')

def courses(request):
    context_object_name = 'courses'    
    chaps=Physics.objects.all()
    img1=phyimg()
    img1.img='static\images\physics2.jpg'
    return render(request,'index.html',{'chaps':chaps,'img1':img1})

def chemistry(request):
    chaps=Chemistry.objects.all()
    img1=chemimg()
    img1.img='static\images\chemistry4.jpg'
    return render(request,'index.html',{'chaps':chaps,'img1':img1})    

def maths(request):
    chaps=Mathamatics.objects.all()
    img1=mathimg()
    img1.img='static\images\maths2.jpg'
    return render(request,'index.html',{'chaps':chaps,'img1':img1}) 

class Contact(CreateView):
    template_name='contact.html'
    model=Contact
    fields='__all__'    
    success_url=reverse_lazy("maths")

