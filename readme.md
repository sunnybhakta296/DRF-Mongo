# DRF + MongoDB (MongoEngine) CRUD Example

This guide walks you through setting up a Django REST Framework (DRF) project with MongoDB using MongoEngine, including CRUD operations for Products, Users, and Orders.

---

## 1. Setup and Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate
pip install django djangorestframework mongoengine djongo

pip freeze > requirements.txt
pip install -r requirements.txt
```

---

## 2. Create Django Project & App

```bash
django-admin startproject shop
cd shop
python manage.py startapp api
```

---

## 3. Configure MongoDB Connection

Edit `shop/settings.py`:

- Remove or ignore the default `DATABASES` setting (MongoDB is external).
- Add MongoEngine connection setup:

```python
# settings.py
from mongoengine import connect

connect(
    db='mydb',
    host='mongodb://localhost:27017/mydb',
)
```

---

## 4. Migrate and Run

```bash
python manage.py migrate
```

---

## 5. Set DRF Renderer Classes

In `settings.py`, configure DRF to use only JSONRenderer for JSON responses:

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # Optionally remove BrowsableAPIRenderer for pure JSON
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}
```

---

## 6. Start Development Server

```bash
python manage.py runserver
```

---

## 7. API Endpoints

Your API will be available at:

- `http://localhost:8000/api/users/`
- `http://localhost:8000/api/products/`
- `http://localhost:8000/api/orders/`

---

## 8. Run Tests

```bash
python manage.py test
```
