
# Matrix Sols – Developer Task

## 📝 Notes API (Django + DRF)

This is a simple Notes REST API that allows users to register, log in, and create/view their own personal notes securely using JWT Authentication.

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd notes_app
```

### 2. Install dependencies

Make sure you're using a virtual environment. Then install:

```bash
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

### 5. Run the development server

```bash
python manage.py runserver
```

---

## 🔐 User Registration & Authentication

### ✳️ Register a new user

**POST** `/api/register/`

```json
{
    "username": "testuser",
    "password": "testpass123"
}
```

### 🔐 Obtain JWT Token

**POST** `/api/token/`

```json
{
    "username": "testuser",
    "password": "testpass123"
}
```

This will return:

```json
{
    "refresh": "your-refresh-token",
    "access": "your-access-token"
}
```

---

## 📲 API Usage (Authenticated Requests)

All requests below require the `Authorization` header with the access token:

```
Authorization: Bearer <your-access-token>
```

### ✅ List all notes (GET)

**GET** `/apis/notes_views/`

Returns a list of notes created by the authenticated user.

---

### 🆕 Create a new note (POST)

**POST** `/apis/notes_views/`

```json
{
    "title": "My First Note",
    "content": "This is the content of my note."
}
```

---

## 📘 API Summary

| Endpoint                  | Method | Auth Required | Description                        |
|---------------------------|--------|----------------|------------------------------------|
| `/api/register/`          | POST   | ❌             | Register a new user                |
| `/api/token/`             | POST   | ❌             | Get JWT token                      |
| `/apis/notes_views/`      | GET    | ✅             | List all personal notes            |
| `/apis/notes_views/`      | POST   | ✅             | Create a new personal note         |

---

## 🛠️ Built With

- Django
- Django REST Framework
- djangorestframework-simplejwt
