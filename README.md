![Django](https://img.shields.io/badge/Django-6.0.2-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

# 🎓   Student Management System  (Django)

A complete Django-based Student Management System built during Class-38.  
This project allows users to add, edit, update, delete, and manage student information with image upload support.

---

## 🚀 Features

- ✅ Add New Student
- ✅ Edit Student Information
- ✅ Delete Student
- ✅ Upload & Update Profile Picture
- ✅ Country Selection
- ✅ Gender Selection
- ✅ Message Field
- ✅ Django Admin Panel
- ✅ Media & Static File Handling

---

## 🛠 Tech Stack

### 🔹 Programming Language
- Python 3

### 🔹 Backend Framework
- Django 6.0.2

### 🔹 Image Handling
- Pillow (for image upload & processing)

### 🔹 Database
- SQLite3 (Default Django Database)

### 🔹 Frontend
- HTML5
- CSS3

### 🔹 Version Control
- Git
- GitHub



---

## 📂 Project Structure

```
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
```


## ⚙️ Installation & Setup

---

### 1️⃣ Clone Repository

```bash
git clone https://github.com/officialontar/Class-39.git
cd Class-39/core
2️⃣ Create Virtual Environment
python -m venv .venv

Activate:

Windows

.venv\Scripts\activate

Mac/Linux

source .venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Migrations
python manage.py migrate
5️⃣ Create Superuser (Optional)
python manage.py createsuperuser
6️⃣ Run Server
python manage.py runserver

Visit:

http://127.0.0.1:8000/

Admin Panel:

http://127.0.0.1:8000/admin/
📸 Screenshots

(Add project screenshots here)

```


## ✨ Admin Panel Highlights

- Custom List Display  
- Image Thumbnail Preview  
- Search Functionality  
- Filter by Gender  
- Filter by Country  
- Proper Formatted Display using Django Choices  

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


```


✨ Admin Customization Highlights

Custom list display

Image thumbnail preview

Search functionality

Filtering by Gender & Country

Proper formatted display using Django choices

📌 Key Learning Outcomes

Django Model & ORM

Django Admin Customization

Template Rendering

Image Upload Handling

CRUD Implementation

Git & GitHub Workflow

Clean UI Structuring


## 👤 Author

**MD. ANISUJJAMAN ONTAR**  
GitHub: https://github.com/officialontar

---

## ⭐ Project Status

✅ Completed (Class-39 Final Version)


📄 License

This project is built for educational and portfolio purposes.