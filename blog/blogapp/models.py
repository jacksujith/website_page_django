from django.db import models

#Create your models here.
# class Userdata(models.Model):
#     firstname = models.CharField(max_length=200)
#     lastname= models.CharField(max_length=122)
#     username = models.CharField(max_length=150)
#     email = models.EmailField()
#     city = models.CharField(max_length=122)
#     password = models.CharField(max_length=12)
#     password2 = models.CharField(max_length=12)
    
    
# def __str__(self):
#     return self.username


class basemax(models.Model):
    firstname = models.CharField(max_length=200)
    lastname= models.CharField(max_length=122)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    city = models.CharField(max_length=122)
    password = models.CharField(max_length=12)
    password2 = models.CharField(max_length=12)
   
    

    def __str__(self):
        return f"{self.firstname}"  
