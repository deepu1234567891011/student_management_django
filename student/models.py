from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=100)
    description=models.TextField()
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

