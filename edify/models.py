from django.db import models

# Create your models here.
class Mathamatics(models.Model):
    
    name:models.CharField(max_length=100)
    topic1=models.CharField(max_length=100)
    link1=models.URLField(max_length=200)
    link2=models.URLField(max_length=200)
    link3=models.URLField(max_length=200)
    def _str_(self):
        return self.name + ' | ' + self.topic1  

class Physics(models.Model):
    
    name:models.CharField(max_length=100)
    topic1=models.CharField(max_length=100)
    channel1=models.CharField(max_length=100)
    link1=models.URLField(max_length=200)
    channel2=models.CharField(max_length=100)
    link2=models.URLField(max_length=200)
    channel3=models.CharField(max_length=100)
    link3=models.URLField(max_length=200)
    def _str_(self):
        return self.topic1 

class Chemistry(models.Model):
    
    name:models.CharField(max_length=100)
    topic1=models.CharField(max_length=100)
    channel1=models.CharField(max_length=100)
    link1=models.URLField(max_length=200)
    channel2=models.CharField(max_length=100)
    link2=models.URLField(max_length=200)
    channel3=models.CharField(max_length=100)
    link3=models.URLField(max_length=200)
    def _str_(self):
        return self.name + ' | ' + self.topic1    

class Contact(models.Model):
    
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=10)
    desc=models.TextField()

    def _str_(self):
        return self.name  

class phyimg() :
    img:str

class chemimg() :
    img:str    
                  
