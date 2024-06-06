# forms.py
from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('student', 'amount', 'payment_date')
# forms.py

# forms.py

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'hostel', 'room_number', 'phone_number', 'home_address', 'father_name', 'father_phone_number']
