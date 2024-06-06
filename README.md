# Hostel-Admin
This Django project is a web-based application designed to manage hostels, students, rooms, and payments efficiently. The application includes functionality for viewing hostels and students, adding students, and managing payment records.
Clone the repository:

git clone
cd hostel-management-system
Create a virtual environment:

python3 -m venv env
source env/bin/activate
Install the dependencies:

pip install -r requirements.txt
Apply the migrations:

python manage.py migrate
Create a superuser:

python manage.py createsuperuser
Run the development server:

python manage.py runserver
Access the application:
Open your browser and go to http://127.0.0.1:8000/.

Folders:


hostel-management-system/
├── hostel_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── add_student.html
│   │   ├── hostel_detail.html
│   │   ├── hostel_list.html
│   │   ├── index.html
│   │   ├── payment_form.html
│   │   ├── payment_history.html
│   │   ├── payment_list.html
│   │   ├── student_detail.html
│   │   ├── student_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── hostel_management/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
