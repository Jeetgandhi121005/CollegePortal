from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student, Course
from .forms import StudentForm

# ==========================================
# Practical 3: Display "Welcome to Django" Using HttpResponse()
# ==========================================
def welcome_http(request):
    return HttpResponse("<div style='font-family:sans-serif;text-align:center;padding:50px;'><h1>Welcome to Django</h1><p><a href='/'>← Back to Portal</a></p></div>")

# ==========================================
# Practical 4: Sending Data from URL to View (URL Parameters)
# ==========================================
def contact_param(request, name):
    return HttpResponse(f"<div style='font-family:sans-serif;text-align:center;padding:50px;'><h2>URL Parameter Received</h2><p style='font-size:24px;color:#0d6efd;'><strong>Student Name :</strong> {name}</p><p><a href='/'>← Back to Portal</a></p></div>")

# ==========================================
# Practical 5: Mapping Multiple Views to URLs (HttpResponse)
# ==========================================
def http_home(request):
    return HttpResponse("Home Page")

def http_about(request):
    return HttpResponse("About Us")

def http_contact(request):
    return HttpResponse("Contact Us")

# ==========================================
# Practical 6, 16, 17, 24: Main Home Page with Master Layout & Template Data
# ==========================================
def home(request):
    data = {
        'name': 'Jeet Gandhi',
        'college': 'JG University',
        'course': 'Python Django'
    }
    return render(request, 'index.html', {'data': data})

# ==========================================
# Practical 7: Inject Data from View to Template
# ==========================================
def student(request):
    data = {
        'name': 'Jeet Gandhi',
        'course': 'BCA',
        'college': 'JG University'
    }
    return render(request, 'student.html', data)

# ==========================================
# Practical 8: Display Student List using Django for Loop
# ==========================================
def students_loop(request):
    student_list = [
        "Jeet Gandhi",
        "Rahul Patel",
        "Priya Shah",
        "Amit Kumar",
        "Neha Joshi"
    ]
    return render(request, 'students.html', {
        'students': student_list
    })

# ==========================================
# Practical 9: Display Course List using forloop.counter
# ==========================================
def courses(request):
    course_list = [
        "Python",
        "Django",
        "HTML & CSS",
        "Android",
        "Angular"
    ]
    return render(request, 'course.html', {
        'courses': course_list
    })

# ==========================================
# Practical 10: Display Pass or Fail using if Statement
# ==========================================
def marks(request):
    marks_val = int(request.GET.get('marks', 72))
    return render(request, 'marks.html', {
        'marks': marks_val
    })

# ==========================================
# Practical 11: Display Result using if...else
# ==========================================
def result(request):
    marks_val = int(request.GET.get('marks', 30))
    return render(request, 'result.html', {
        'marks': marks_val
    })

# ==========================================
# Practical 12: Grade Calculator using if...elif...else
# ==========================================
def grade(request):
    marks_val = int(request.GET.get('marks', 82))
    return render(request, 'grade.html', {
        'marks': marks_val
    })

# ==========================================
# Practical 13: Employee Salary Status (Nested if inside for Loop)
# ==========================================
def employee(request):
    employees = [
        {"name": "Rahul Patel", "salary": 25000},
        {"name": "Priya Shah", "salary": 65000},
        {"name": "Amit Kumar", "salary": 45000},
        {"name": "Jeet Gandhi", "salary": 55000},
    ]
    return render(request, 'employee.html', {
        'employees': employees
    })

# ==========================================
# Practical 14: Empty List Example using {% empty %}
# ==========================================
def books(request):
    show_sample = request.GET.get('sample')
    if show_sample == '1':
        book_list = ["Python Programming", "Django for Web Development", "HTML & CSS Guide"]
    else:
        book_list = []
    return render(request, 'books.html', {
        'books': book_list,
        'has_sample': bool(show_sample)
    })

# ==========================================
# Practical 15: Using Django Template Filters
# ==========================================
def filters(request):
    message = request.GET.get('msg', 'welcome to django framework')
    return render(request, 'filter.html', {
        'message': message,
        'name': 'jeet gandhi',
        'college': 'jg university',
        'course': 'python django'
    })

# ==========================================
# Practical 16: Using Multiple Templates (About & Contact)
# ==========================================
def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')
        messages.success(request, f"Thank you, {name}! Your message has been sent successfully.")
        return redirect('contact')
    return render(request, 'contact.html')

# ==========================================
# Practical 20: Create and Display a Django Form 'Student'
# ==========================================
def student_form(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Student registered successfully via Django Form!')
        return redirect('student_list')
    return render(request, 'student/student_django_form.html', {'form': form})

# ==========================================
# Practical 21: STUDENT CRUD with FBV on Student Table
# ==========================================
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/list.html', {'students': students})

def add_student(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        course_id = request.POST.get('course')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        city = request.POST.get('city')

        if not course_id:
            messages.error(request, "Please select a valid course.")
            return render(request, 'student/student_form.html', {'courses': courses})

        course = get_object_or_404(Course, id=course_id)
        Student.objects.create(
            name=name,
            course=course,
            email=email,
            mobile=mobile,
            city=city
        )
        messages.success(request, f"Student {name} registered successfully!")
        return redirect('student_list')

    return render(request, 'student/student_form.html', {'courses': courses})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.all()
    if request.method == 'POST':
        student.name = request.POST.get('name')
        course_id = request.POST.get('course')
        student.course = get_object_or_404(Course, id=course_id)
        student.email = request.POST.get('email')
        student.mobile = request.POST.get('mobile')
        student.city = request.POST.get('city')
        student.save()
        messages.success(request, f"Student {student.name} updated successfully!")
        return redirect('student_list')

    return render(request, 'student/edit.html', {'student': student, 'courses': courses})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student_name = student.name
    student.delete()
    messages.success(request, f"Student {student_name} deleted successfully.")
    return redirect('student_list')

# ==========================================
# Practical 22: Course CRUD with Class Based Views (CBV) and Search
# ==========================================
class CourseListView(ListView):
    model = Course
    template_name = 'student/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        query = self.request.GET.get('search')
        courses = Course.objects.all()
        if query:
            courses = courses.filter(course_name__icontains=query)
        return courses

class CourseCreateView(CreateView):
    model = Course
    fields = ['course_name', 'course_code', 'start_date', 'end_date', 'faculty_name', 'is_active']
    template_name = 'student/course_form.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        messages.success(self.request, "Course created successfully!")
        return super().form_valid(form)

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['course_name', 'course_code', 'start_date', 'end_date', 'faculty_name', 'is_active']
    template_name = 'student/course_form.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        messages.success(self.request, "Course updated successfully!")
        return super().form_valid(form)

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'student/course_delete.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        messages.success(self.request, "Course deleted successfully!")
        return super().form_valid(form)

# ==========================================
# Practical 23: Create, Modify and Delete Django Sessions
# ==========================================
def create_session(request):
    request.session['student_name'] = 'Jeet Gandhi'
    request.session['course'] = 'Python Django'
    messages.success(request, "Session created successfully! (student_name='Jeet Gandhi', course='Python Django')")
    return redirect('show_session')

def modify_session(request):
    request.session['course'] = 'Django Framework Advanced'
    messages.info(request, "Session modified successfully! (course changed to 'Django Framework Advanced')")
    return redirect('show_session')

def delete_session(request):
    request.session.flush()
    messages.warning(request, "Session cleared and deleted successfully!")
    return redirect('show_session')

def show_session(request):
    name = request.session.get('student_name', 'No Session Active')
    course = request.session.get('course', 'No Session Active')
    return render(request, 'session.html', {'name': name, 'course': course})

# ==========================================
# Practical 24: Django Authentication - Login and Logout
# ==========================================
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

# ==========================================
# Practical 25: Check Email ID Exists using AJAX jQuery
# ==========================================
def check_email(request):
    email = request.GET.get('email', '').strip()
    exists = Student.objects.filter(email__iexact=email).exists() if email else False
    return JsonResponse({'exists': exists})

def check_email_page(request):
    return render(request, 'check_email.html')

# ==========================================
# Practicals Index / College Lab Guide
# ==========================================
def practicals_index(request):
    return render(request, 'practicals_index.html')
