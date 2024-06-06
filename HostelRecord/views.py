from django.shortcuts import render
from .models import Hostel, Student, Room, Payment

def index(request):
    hostels = Hostel.objects.all()
    return render(request, 'index.html', {'hostels': index})


from django.shortcuts import render
from .models import Hostel

def hostel_list(request):
    hostels = Hostel.objects.all()
    return render(request, 'hostel_list.html', {'hostels': hostels})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment

def payment_create(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payment_form.html', {'form': form})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})

from django.shortcuts import render
from .models import Payment

def payment_history(request):
    payments = Payment.objects.all()
    payment_history = {}
    for payment in payments:
        month = payment.date.strftime('%B %Y')
        if month not in payment_history:
            payment_history[month] = []
        payment_history[month].append(payment)
    return render(request, 'payment_history.html', {'payment_history': payment_history})

def payment_history(request, hostel_id):
    hostel = Hostel.objects.get(id=hostel_id)
    payments = Payment.objects.filter(student__room__hostel=hostel)
    payment_history = {}
    for payment in payments:
        month = payment.date.strftime('%B %Y')
        if month not in payment_history:
            payment_history[month] = []
        payment_history[month].append(payment)
    return render(request, 'payment_history.html', {'payment_history': payment_history, 'hostel': hostel})
# views.py

from django.shortcuts import render, get_object_or_404
from .models import Hostel, Student

def hostel_list(request):
    hostels = Hostel.objects.all()
    return render(request, 'hostel_list.html', {'hostels': hostels})

def hostel_detail(request, hostel_id):
    hostel = get_object_or_404(Hostel, id=hostel_id)
    students = Student.objects.filter(hostel_id=hostel_id)  # Assuming 'hostel_id' is the foreign key field
    return render(request, 'hostel_detail.html', {'hostel': hostel, 'students': students})
# views.py

from django.shortcuts import render, get_object_or_404
from .models import Hostel, Student

def hostel_detail(request, hostel_id):
    hostel = get_object_or_404(Hostel, id=hostel_id)
    students = Student.objects.filter(hostel_id=hostel_id)
    return render(request, 'hostel_detail.html', {'hostel': hostel, 'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})
# views.py

from django.shortcuts import render, get_object_or_404
from .models import Hostel, Student

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})
# views.py

from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Replace with the URL name for the student list page
    else:
        form = StudentForm()
    
    return render(request, 'add_student.html', {'form': form})
