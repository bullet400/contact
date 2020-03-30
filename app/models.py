from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    Manager =models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    firstname = models.CharField(max_length=50)
    middlename =models.CharField(max_length=50)
    lastname =models.CharField(max_length=50)
    email =models.EmailField(max_length=50)
    phone =models.IntegerField()
    info =models.TextField(default="Please enter info here")
    gender =models.CharField(max_length=20, choices=(
            ('male','Male'),
            ('female', 'Female'))
            
            )
    image =models.ImageField(upload_to='images/', blank=True)    
    datecreated =models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.lastname

    def fullname(self):
        fullname= self.firstname +" "+self.middlename+" " +self.lastname
        return fullname

    def user_email(self):
        return self.email[10]