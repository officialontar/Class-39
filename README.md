![Django](https://img.shields.io/badge/Django-6.0.2-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

# 🎓 Class-38 Django Student Management System

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

- Python 3
- Django 6.0.2
- Pillow
- SQLite3
- HTML5
- CSS3

---

## 📂 Project Structure

```
Class-38/
│
├── core/                 # Django project settings
├── student_info/         # Main app
├── templates/            # HTML Templates
├── static/               # CSS & Static files
├── media/                # Uploaded Images
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/officialontar/Class-38.git
cd Class-38/core
```

### 2️⃣ Create Virtual Environment (Windows)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

### 5️⃣ Run Development Server

```bash
python manage.py runserver
```

Visit in your browser:

```
http://127.0.0.1:8000/
```

---

## 📸 Image Upload Feature

This project supports:

- Uploading student profile images
- Updating images
- Media file configuration in Django

---

## 🔐 Admin Panel Access

Create superuser:

```bash
python manage.py createsuperuser
```

Then visit:

```
http://127.0.0.1:8000/admin/
```

---

## 👤 Author

**MD. ANISUJJAMAN ONTAR**  
GitHub: https://github.com/officialontar

---

## ⭐ Project Status

✅ Completed (Class-38 Final Version)