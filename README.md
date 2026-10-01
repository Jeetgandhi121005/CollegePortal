# 🎓 College Portal - Student Management System (Django 5.x)

A modern, full-stack **Student Management System** built with Python and the Django Framework, covering all 25 college assignment practicals and questions from scratch.

---

## 🌟 Project Highlights & Features

- **Design System:** Sleek Navy/Deep-Blue theme, responsive UI cards, clean typography (Inter), rounded badges, smooth animations.
- **FBV Student CRUD:** Create, Read, Update, Delete students with relational Course mapping.
- **CBV Course CRUD & Search:** `ListView`, `CreateView`, `UpdateView`, `DeleteView` + live keyword search filter.
- **Real-Time AJAX (jQuery):** Asynchronous live email duplicate verification without page reload.
- **Django Authentication:** User Login, Logout, protected routes, and session integration.
- **Session Management:** Full interactive session state tester (`create`, `modify`, `delete`, `show`).
- **Template Logic & Filters:** Conditional branching (`if`, `if-else`, `if-elif-else`), `for` loops, `forloop.counter`, `{% empty %}`, template filters (`upper`, `lower`, `capfirst`, `truncatechars`, `length`).
- **Production Ready:** Pre-configured with `whitenoise`, `gunicorn`, `Procfile`, `runtime.txt`, and `requirements.txt` for fast deployment.

---

## 🚀 Quick Start (Run Locally)

### 1. Prerequisites
Ensure Python 3.10+ is installed:
```bash
python --version
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Migrations & Seed Sample Data
```bash
python manage.py migrate
python seed_data.py
```
*(Pre-seeds default courses, students, and admin/jeet user accounts)*

### 4. Start Development Server
```bash
python manage.py runserver
```
Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser.

---

## 🔑 Default Login & Admin Credentials

| Role | Username | Password | Email |
| :--- | :--- | :--- | :--- |
| **Superuser / Admin** | `admin` | `admin123` | `admin@collegeportal.com` |
| **Student / User** | `jeet` | `jeet123` | `jeet@gmail.com` |

---

## 📋 Complete Practical / Questions Mapping (1 to 25)

| Practical # | Title / Concept | Route / URL | Description |
| :--- | :--- | :--- | :--- |
| **1 & 2** | Environment Setup & App Config | `/` | Python, Django, and `student` app configured in `INSTALLED_APPS` |
| **3** | HttpResponse "Welcome to Django" | `/welcome-http/` | Direct `HttpResponse("<h1>Welcome to Django</h1>")` view |
| **4** | URL Parameters | `/contact/jeet/` | Dynamic parameterized routing `path('contact/<str:name>/')` |
| **5** | Mapping Multiple Views to URLs | `/http-demo/home/` | Multiple view functions returning plain text/HTML responses |
| **6** | Template Rendering | `/` | Render `index.html` template using `render()` |
| **7** | Inject Data from View to Template | `/student/` | Passing context dict to `student.html` |
| **8** | Student List with For Loop | `/students-loop/` | Iterating arrays with `{% for student in students %}` |
| **9** | Course List with `forloop.counter` | `/courses/` | Styled cards with `course.css` and counter tags |
| **10** | Pass/Fail (`if` statement) | `/marks/` | Conditional check `{% if marks >= 35 %}` |
| **11** | Result (`if...else`) | `/result/` | Binary branch `{% if marks >= 35 %}Pass{% else %}Fail{% endif %}` |
| **12** | Grade Calculator (`if...elif...else`) | `/grade/` | Multi-condition grading (Distinction / First Class / Pass / Fail) |
| **13** | Employee Salary Status | `/employee/` | Nested `if` within `for` loop (High Salary > 40000 vs Normal) |
| **14** | Empty List Example (`{% empty %}`) | `/books/` | Graceful fallback when list contains zero elements |
| **15** | Django Template Filters | `/filters/` | `|upper`, `|lower`, `|capfirst`, `|truncatechars`, `|length` |
| **16** | Using Multiple Templates | `/`, `/about/`, `/contact/` | Distinct template files for multiple pages |
| **17** | Extending Templates (Master Layout) | `base.html` | Master navbar, footer, container block inheritance |
| **18** | Static Files (CSS & Images) | `/static/` | `style.css`, `logo.png`, `student.png` assets |
| **19** | Adding JavaScript File | `script.js` | Alert function `showMessage()` and DOM interaction |
| **20** | Django ModelForm 'Student' | `/student-form/` | `StudentForm(forms.ModelForm)` rendered with `{{ form.as_p }}` |
| **21** | Student CRUD with FBV | `/students/` | Full Create, Read, Update, Delete using Function-Based Views |
| **22** | Course CRUD with CBV & Search | `/course-list/` | `ListView`, `CreateView`, `UpdateView`, `DeleteView` + search query |
| **23** | Django Session Management | `/session/show/` | Create, Modify, Delete, and Display session data |
| **24** | Django Authentication | `/login/` | User login, logout, and authentication flow |
| **25** | AJAX jQuery Email Check | `/check-email-page/` | Real-time email duplicate check via `JsonResponse` |
| **Hub** | **Practicals Showcase Index** | `/practicals/` | **Interactive index to browse & test all practicals** |

---

## 🌐 Deployment Guide

### Option A: Free Deployment on Render (Recommended)
1. Push this project folder to a GitHub repository.
2. Log in to [Render](https://render.com) and click **New +** → **Web Service**.
3. Select your GitHub repository.
4. Set the following parameters:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt && python manage.py migrate && python seed_data.py`
   - **Start Command:** `gunicorn djangoproject.wsgi:application`
5. Click **Create Web Service**. Your portal will be live on a `https://<app-name>.onrender.com` URL!

### Option B: Free Deployment on PythonAnywhere
1. Create a free account on [PythonAnywhere](https://www.pythonanywhere.com/).
2. Open a **Bash Console** and clone/upload your project.
3. In the **Web** tab, create a Manual Django configuration with Python 3.10+.
4. Point the WSGI configuration to `djangoproject/wsgi.py` and set static directory to `/static/`.
5. Reload the web app.

---

## 📁 Project Structure

```
College Portal/
├── djangoproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── student/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── student.html
│   ├── students.html
│   ├── course.html
│   ├── marks.html
│   ├── result.html
│   ├── grade.html
│   ├── employee.html
│   ├── books.html
│   ├── filter.html
│   ├── session.html
│   ├── login.html
│   ├── check_email.html
│   ├── practicals_index.html
│   └── student/
│       ├── list.html
│       ├── student_form.html
│       ├── edit.html
│       ├── student_django_form.html
│       ├── course_list.html
│       ├── course_form.html
│       └── course_delete.html
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── course.css
│   ├── images/
│   │   ├── logo.png
│   │   └── student.png
│   └── js/
│       └── script.js
├── manage.py
├── seed_data.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── .gitignore
├── db.sqlite3
└── README.md
```
