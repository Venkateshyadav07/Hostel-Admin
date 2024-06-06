from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('hostels/', views.hostel_list, name='hostel_list'),
    path('students/', views.student_list, name='student_list'),
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/create/', views.payment_create, name='payment_create'),
    path('hostels/', views.hostel_list, name='hostel_list'),
    path('hostels/<int:hostel_id>/', views.hostel_detail, name='hostel_detail'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('add-student/', views.add_student, name='add_student'),
]