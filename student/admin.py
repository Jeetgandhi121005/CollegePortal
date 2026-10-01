from django.contrib import admin
from .models import Course, Student

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'faculty_name', 'start_date', 'end_date', 'is_active')
    search_fields = ('course_name', 'course_code', 'faculty_name')
    list_filter = ('is_active',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'email', 'mobile', 'city')
    search_fields = ('name', 'email', 'mobile', 'city')
    list_filter = ('course', 'city')
