from datetime import date
from django.db import models

# Create your models here.

class Role(models.Model):
    role_title = models.CharField(max_length=100, verbose_name="Role")
    role_description = models.TextField()

    def __str__(self):
        return self.role_title


class Employee(models.Model):
    name = models.CharField(max_length=150, verbose_name="Full names")
    email = models.EmailField()
    date_of_birth = models.DateField()
    address = models.CharField(max_length=250)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

 
class LeaveType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Leave")
    description = models.TextField()

    def __str__(self):
        return self.name


class Leave(models.Model):
    STATUS = (
        ('APPROVED', 'Approved'),
        ('REJECTED','Rejected'),
        ('PENDING', 'Pending')
    )

    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS, default="PENDING")
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    applied_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee.name} - {self.type.name}'



