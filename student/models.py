from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    faculty_name = models.CharField(max_length=100, default="Prof. Mehta")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
