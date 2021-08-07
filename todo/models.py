from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Name (models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Task (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    sub=models.ForeignKey(Name, on_delete=models.SET_NULL, null=True)
    chapter=models.CharField(max_length=200)
    details=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.chapter

    class Meta:
        ordering=['complete']
        
