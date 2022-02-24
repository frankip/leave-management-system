import email
from operator import mod
from unicodedata import name
from django.db import models

# Create your models here.

class Role(models.Model):
    role_title = models.CharField(max_length=100)
    role_description = models.TextField()

    def __str__(self):
        return self.role_title

class Employee(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    date_of_birth = models.DateField()
    address = models.CharField(max_length=250)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def _str__(self):
        return self.name

class LeaveType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name



class Leave(models.Model):
    STATUS = (
        ('APPROVED', 'Approved'),
        ('REJECTED','Rejected'),
        ('PENDING', 'Pending')
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS)
    start_date = models.DateField()
    end_date = models.DateField()
    applied_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.employee + self.type 



