import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')
django.setup()

from django.contrib.auth.models import User
from student.models import Course, Student
from datetime import date

# 1. Create superuser if not exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@collegeportal.com', 'admin123')
    print("Created superuser: admin / admin123")

if not User.objects.filter(username='jeet').exists():
    u = User.objects.create_user('jeet', 'jeet@gmail.com', 'jeet123')
    print("Created user: jeet / jeet123")

# 2. Seed Courses
courses_data = [
    {"code": "PY101", "name": "Python Django", "faculty": "Prof. Mehta", "start": date(2026, 1, 15), "end": date(2026, 6, 15)},
    {"code": "WD102", "name": "HTML & CSS", "faculty": "Prof. Shah", "start": date(2026, 2, 1), "end": date(2026, 5, 30)},
    {"code": "NG103", "name": "Angular", "faculty": "Prof. Patel", "start": date(2026, 3, 10), "end": date(2026, 8, 10)},
    {"code": "AND104", "name": "Android", "faculty": "Prof. Dave", "start": date(2026, 2, 20), "end": date(2026, 7, 20)},
    {"code": "BS105", "name": "Bootstrap", "faculty": "Prof. Joshi", "start": date(2026, 4, 1), "end": date(2026, 6, 30)},
]

for c in courses_data:
    obj, created = Course.objects.get_or_create(
        course_code=c["code"],
        defaults={
            "course_name": c["name"],
            "faculty_name": c["faculty"],
            "start_date": c["start"],
            "end_date": c["end"],
            "is_active": True
        }
    )
    if created:
        print(f"Created Course: {obj.course_name}")

# 3. Seed Students
py_course = Course.objects.get(course_code="PY101")
html_course = Course.objects.get(course_code="WD102")
ng_course = Course.objects.get(course_code="NG103")

students_data = [
    {"name": "Jeet Gandhi", "course": py_course, "email": "jeet@gmail.com", "mobile": "9876543210", "city": "Ahmedabad"},
    {"name": "Rahul Patel", "course": html_course, "email": "rahul@gmail.com", "mobile": "9898989898", "city": "Vadodara"},
    {"name": "Priya Shah", "course": ng_course, "email": "priya@gmail.com", "mobile": "9988776655", "city": "Surat"},
    {"name": "Amit Kumar", "course": py_course, "email": "amit@gmail.com", "mobile": "9876500001", "city": "Ahmedabad"},
    {"name": "Neha Joshi", "course": html_course, "email": "neha@gmail.com", "mobile": "9876500002", "city": "Rajkot"},
]

for s in students_data:
    obj, created = Student.objects.get_or_create(
        email=s["email"],
        defaults={
            "name": s["name"],
            "course": s["course"],
            "mobile": s["mobile"],
            "city": s["city"]
        }
    )
    if created:
        print(f"Created Student: {obj.name}")

print("Seeding completed successfully!")
