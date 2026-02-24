![Django](https://img.shields.io/badge/Django-6.0.2-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)




# 🎓 Student Management System (Django)

A complete Django-based Student Management System built with full CRUD functionality, admin customization, image upload, filtering, and clean UI design. This project is designed to demonstrate practical Django development skills and proper project structuring.

---

## 🚀 Features

- ✅ Add Student
- ✅ View All Students
- ✅ Student Profile Card View
- ✅ Edit Student Information
- ✅ Delete Student
- ✅ Upload Profile Picture
- ✅ Gender & Country Choices Formatting
- ✅ Django Admin Panel Customization
- ✅ Image Thumbnail Preview in Admin
- ✅ Filter by Gender & Country
- ✅ Search Functionality in Admin
- ✅ Clean UI with Custom Styling

---

## 🛠 Tech Stack

- Backend: Django
- Frontend: HTML5, CSS3
- Database: SQLite3
- Version Control: Git & GitHub

---

## 📂 Project Structure

core/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── student_info/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│   ├── apps.py
│   └── migrations/
│
├── templates/
│   ├── base.html
│   └── student_info/
│       ├── add_student.html
│       ├── edit_student.html
│       ├── all_student.html
│       ├── view_student.html
│       └── index.html
│
├── static/
│   └── style.css
│
└── media/
    └── students/

---

## ⚙️ Installation & Setup Guide

### 1️⃣ Clone the Repository

git clone https://github.com/officialontar/Class-39.git  
cd Class-39/core  

---

### 2️⃣ Create Virtual Environment

Windows:
python -m venv .venv  
.venv\Scripts\activate  

Mac/Linux:
python3 -m venv .venv  
source .venv/bin/activate  

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt  

---

### 4️⃣ Apply Migrations

python manage.py migrate  

---

### 5️⃣ Create Superuser (Optional)

python manage.py createsuperuser  

---

### 6️⃣ Run Development Server

python manage.py runserver  

Visit:
http://127.0.0.1:8000/  

Admin Panel:
http://127.0.0.1:8000/admin/  

---

## 📸 Screenshots

(Add your project screenshots here for better presentation)

---

## ✨ Admin Panel Highlights

- Custom List Display
- Image Thumbnail Preview
- Search Functionality
- Filter by Gender
- Filter by Country
- Proper formatted display using Django Choices

---

## 📌 Key Learning Outcomes

- Django Models & ORM
- Django Admin Customization
- Template Rendering
- Image Upload Handling
- CRUD Operations
- Clean Project Structure
- Git & GitHub Workflow
- UI Styling with CSS

---


## 👤 Author

**MD. ANISUJJAMAN ONTAR**  
GitHub: https://github.com/officialontar

---

## ⭐ Project Status

✅ Completed (Class-39 Final Version)


📄 License

This project is built for educational and portfolio purposes.