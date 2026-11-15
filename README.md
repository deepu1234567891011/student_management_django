# 🎓 Student Management System - Django + MySQL

A complete Student Management System built using Python Django and MySQL Database. This project manages student records with authentication, dashboard and full CRUD functionality.

## ✨ Features
- 🔐 User Registration and Login System
- 📊 Dashboard to Manage Students
- ➕ Add New Student with Details
- ✏️ Edit / Update Student Information
- ❌ Delete Student Records
- 🔍 Search Students by Name / ID
- 🎨 Clean UI with CSS

## 🛠️ Tech Stack
- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Django Templates
- **Database:** MySQL
- **Tools:** Git, GitHub, VS Code, MySQL Workbench

## 📁 Folder Structure
- student_management/ - Main Django Project (settings.py)
- student/ - Django App (models, views, urls)
- student/templates/ - login.html, dashboard.html etc.
- student/static/css/ - style.css
- manage.py - Django Main File
- requirements.txt - Dependencies

## 🚀 How To Run This Project

1. Clone this repository
   git clone (https://github.com/deepu1234567891011/student_management_django/tree/main)

2. Go inside folder
   cd Student-_management-_django-project

3. Create virtual environment
   python -m venv env

4. Activate env (Windows)
   env\Scripts\activate

5. Install requirements
   pip install -r requirements.txt
   pip install mysqlclient

6. Create MySQL Database
   CREATE DATABASE student_db;

7. Update settings.py
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'student_db',
           'USER': 'root',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }

8. Run migrations
   python manage.py migrate

9. Run server
   python manage.py runserver

10. Open browser
    local server will run at this-http://127.0.0.1:8000/

## 👨‍💻 Developed By
Deepu - Python Django + MySQL Developer
GitHub: deepu1234567891011

## 🔮 Future Plans
- Deploy with MySQL on Render / Railway
- Add Student Photo Upload
- Add Attendance & Fees Module

Made with ❤️ using Django & MySQL
