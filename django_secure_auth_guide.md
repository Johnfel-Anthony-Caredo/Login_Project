# Django Secure Registration and Login System Guide

This guide outlines a simple Django implementation for a secure registration and login system that matches the cybersecurity midterm project requirements. The project requires user registration, user login, password hashing, a unique random salt for each user, and a pepper that is hidden in code and never stored in the database [file:1].

## Recommended Stack

The recommended stack for this project is Django for the web framework and SQLite for the database. Django makes it easy to build forms, models, and views, while SQLite is the least-hassle option because it works out of the box with Django and is easy to inspect for screenshots of the stored username, hashed password, and salt [file:1].

## Suggested Project Structure

Use a small Django project with one app dedicated to authentication logic. A custom model is easier to align with the required database screenshot because the project brief specifically expects the database to show username, hashed password, and salt, while the pepper must not appear there [file:1].

```text
secure_auth/
├── manage.py
├── db.sqlite3
├── secure_auth/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── utils.py
│   ├── views.py
│   └── migrations/
└── templates/
    └── accounts/
        ├── register.html
        └── login.html
```

## Database Design

Create a custom table such as `AccountUser` with only the fields needed by the project. The database should store the username, hashed password, and salt, while the pepper must remain hidden in the code or configuration and should never be stored in the table [file:1].

Suggested fields:

- `username` - unique username field.
- `password_hash` - stores the hashed password value.
- `salt` - stores the unique random salt for that user.

## Security Workflow

### Registration Flow

The registration module must accept a username and password, generate a random salt, combine the password with the salt and pepper, hash the result, and store the username, hashed password, and salt in the database [file:1].

Recommended registration logic:

1. Accept `username` and `password` from the form.
2. Generate a unique salt using Python's `secrets` module.
3. Read the pepper from `settings.py` or an environment variable.
4. Compute the hash of `password + salt + pepper`.
5. Save `username`, `password_hash`, and `salt` to SQLite [file:1].

### Login Flow

The login module must retrieve the stored salt for the username, re-apply the hash using the input password plus the stored salt and pepper, and compare it with the stored hash. The system should display `Login Successful` for a match and `Invalid Username or Password` otherwise [file:1].

Recommended login logic:

1. Accept `username` and `password` from the login form.
2. Query the database for the matching username.
3. Retrieve the stored salt.
4. Recompute the hash using `input_password + stored_salt + pepper`.
5. Compare the recomputed hash with the stored `password_hash`.
6. Return the correct success or failure message [file:1].

## Recommended File Responsibilities

Keep the code organized by assigning each file a clear responsibility. This supports the project grading criteria for code quality and organization, and it also makes the project easier to explain during submission [file:1].

### `models.py`

Define the custom user table.

```python
from django.db import models

class AccountUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password_hash = models.CharField(max_length=255)
    salt = models.CharField(max_length=64)

    def __str__(self):
        return self.username
```

### `forms.py`

Create simple forms for registration and login.

```python
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
```

### `utils.py`

Put hashing helpers here so the views stay clean.

```python
import hashlib
import secrets
from django.conf import settings


def generate_salt():
    return secrets.token_hex(16)


def hash_password(password, salt):
    pepper = settings.PASSWORD_PEPPER
    combined = password + salt + pepper
    return hashlib.sha256(combined.encode()).hexdigest()
```

### `views.py`

Use one view for registration and one for login.

```python
from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from .models import AccountUser
from .utils import generate_salt, hash_password


def register_view(request):
    message = ""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            salt = generate_salt()
            password_hash = hash_password(password, salt)
            AccountUser.objects.create(
                username=username,
                password_hash=password_hash,
                salt=salt,
            )
            message = "Registration Successful"
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form, "message": message})


def login_view(request):
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                user = AccountUser.objects.get(username=username)
                computed_hash = hash_password(password, user.salt)
                if computed_hash == user.password_hash:
                    message = "Login Successful"
                else:
                    message = "Invalid Username or Password"
            except AccountUser.DoesNotExist:
                message = "Invalid Username or Password"
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form, "message": message})
```

### `urls.py`

Map the registration and login pages clearly.

```python
from django.urls import path
from .views import register_view, login_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
]
```

## Pepper Placement

The pepper should not be stored in the database because the project explicitly says it must be hidden in the code [file:1]. A practical option is to place it in `settings.py` or load it from an environment variable so the database table only contains the username, hashed password, and salt [file:1].

Example:

```python
PASSWORD_PEPPER = "your_secret_pepper_here"
```

A better classroom-friendly explanation is that the pepper is stored in application configuration, not in the database, so even if someone sees the table contents, the pepper is still missing [file:1].

## Hashing Choice

For this project, SHA-256 is a reasonable choice because the project brief explicitly lists secure hash functions such as SHA-256 and bcrypt as examples [file:1]. Using SHA-256 with a unique random salt per user and a separate pepper makes the logic easy to demonstrate in code, screenshots, and the written documentation [file:1].

## Screenshots to Prepare

The submission requires screenshots of the registration process, login process, and database contents. The database screenshot should show the username, hashed password, and salt, and it must not show the pepper [file:1].

Prepare these screenshots:

1. Registration form input.
2. Successful registration message.
3. Successful login message.
4. Failed login attempt with `Invalid Username or Password`.
5. Database table view showing `username`, `password_hash`, and `salt` only [file:1].

## Why This Structure Works

This structure keeps the project small, easy to debug, and easy to document. It matches the required registration and login behavior, clearly demonstrates hashing with salt and pepper, avoids plain text password storage, and makes the final screenshots and explanation straightforward to prepare [file:1].

## Best Final Recommendation

Use Django, SQLite, a custom `AccountUser` model, a helper function for SHA-256 hashing, random salt generation through the `secrets` module, and a pepper stored in configuration. This is the lowest-hassle setup that still aligns closely with the project instructions and grading criteria [file:1].
