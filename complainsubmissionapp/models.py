from distutils.command.upload import upload
from django.db import models
from django.forms import ImageField

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30, null=False, primary_key=True)
    matricule = models.CharField(max_length=15, null=False)
    complain = models.CharField(max_length=100, null=False)
    prove = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name