from django.db import models





class Room(models.Model):
    number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE)

class Payment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
# models.py

from django.db import models


class Hostel(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    address = models.CharField(max_length=255)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# models.py

from django.db import models
from .models import Hostel

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    home_address = models.CharField(max_length=255)
    father_name = models.CharField(max_length=100)
    father_phone_number = models.CharField(max_length=15)
    payment = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# models.py

from django.db import models
from .models import Hostel


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)  # Add room_number field
    phone_number = models.CharField(max_length=15)
    home_address = models.CharField(max_length=255)
    father_name = models.CharField(max_length=100)
    father_phone_number = models.CharField(max_length=15)
   


    def __str__(self):
        return self.name


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.amount} on {self.payment_date}"
