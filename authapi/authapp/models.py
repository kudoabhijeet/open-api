from django.db import models

# Create your models here.
class users(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.EmailField(max_length=120, unique=True)
    password = models.CharField(max_length=10)
    

    def __str__(self): 
        return self.firstname