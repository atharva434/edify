from django.shortcuts import render,HttpResponse
from .models import Chemistry, Physics,phyimg,chemimg
# Create your views here.
def index(request):

    
    return render(request,'loll.html')

def courses(request):
    chaps=Physics.objects.all()
    img1=phyimg()
    img1.img='static\images\physics.jpg'
    return render(request,'mainpage.html',{'chaps':chaps,'img1':img1})

def chemistry(request):
    chaps=Chemistry.objects.all()
    img1=chemimg()
    img1.img='static\images\chemistry.jpg'
    return render(request,'mainpage.html',{'chaps':chaps,'img1':img1})    



