from django.urls import path
from . import views

urlpatterns = [
    # Main Navigation & Home
    path('', views.home, name='home'),
    path('home/', views.home, name='home_alt'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('practicals/', views.practicals_index, name='practicals'),

    # Practical 3: Welcome using HttpResponse
    path('welcome-http/', views.welcome_http, name='welcome_http'),

    # Practical 4: URL Parameters
    path('contact/<str:name>/', views.contact_param, name='contact_param'),

    # Practical 5: Multiple Views HTTP Mapping
    path('http-demo/home/', views.http_home, name='http_home'),
    path('http-demo/about/', views.http_about, name='http_about'),
    path('http-demo/contact/', views.http_contact, name='http_contact'),

    # Practical 7: Inject Data to Template
    path('student/', views.student, name='student'),

    # Practical 8: Student List with For Loop
    path('students-loop/', views.students_loop, name='students_loop'),

    # Practical 9: Course List
    path('courses/', views.courses, name='course'),

    # Practical 10: Marks If condition
    path('marks/', views.marks, name='marks'),

    # Practical 11: Marks Result If-Else
    path('result/', views.result, name='result'),

    # Practical 12: Grade Calculator If-Elif-Else
    path('grade/', views.grade, name='grade'),

    # Practical 13: Employee Salary Status
    path('employee/', views.employee, name='employee'),

    # Practical 14: Empty List {% empty %}
    path('books/', views.books, name='books'),

    # Practical 15: Django Template Filters
    path('filters/', views.filters, name='filters'),

    # Practical 20: Django Form 'Student'
    path('student-form/', views.student_form, name='student_form'),

    # Practical 21: Student CRUD with FBV
    path('students/', views.student_list, name='student_list'),
    path('add-student/', views.add_student, name='add_student'),
    path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),

    # Practical 22: Course CRUD with CBV & Search
    path('course-list/', views.CourseListView.as_view(), name='course_list'),
    path('course-add/', views.CourseCreateView.as_view(), name='course_add'),
    path('course-edit/<int:pk>/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('course-delete/<int:pk>/', views.CourseDeleteView.as_view(), name='course_delete'),

    # Practical 23: Django Sessions
    path('session/', views.show_session, name='session_root'),
    path('session/create/', views.create_session, name='create_session'),
    path('session/modify/', views.modify_session, name='modify_session'),
    path('session/delete/', views.delete_session, name='delete_session'),
    path('session/show/', views.show_session, name='show_session'),

    # Practical 24: Django Auth (Login/Logout)
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Practical 25: AJAX jQuery Email Check
    path('check-email/', views.check_email, name='check_email'),
    path('check-email-page/', views.check_email_page, name='check_email_page'),
]
