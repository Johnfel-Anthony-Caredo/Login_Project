# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Django 6.0 cybersecurity midterm project implementing a secure registration and login system with SHA-256 hashing, per-user salts, and a global pepper. Uses SQLite for the database and a single `accounts` Django app.

## Commands

```bash
# Activate the virtual environment
env\Scripts\activate

# Start the development server
python manage.py runserver

# Make and apply database migrations
python manage.py makemigrations
python manage.py migrate

# Run the standalone test script
python test_auth.py
```

## Architecture

- **`config/`** — Django project package (settings, root URLconf, ASGI/WSGI).
- **`accounts/`** — Single app containing all authentication logic.
- **`templates/accounts/`** — Django templates for `register.html` and `login.html`.
- **`static/`** — Static files directory.

### Authentication Flow

1. **Registration**: Form input → check for duplicate username → generate random salt via `secrets.token_hex(16)` → hash `password + salt + pepper` with SHA-256 → store `AccountUser(username, password_hash, salt)` in SQLite.
2. **Login**: Form input → query user by username → retrieve stored salt → recompute `hash(input_password + stored_salt + pepper)` → compare against stored `password_hash`.

### Key Design Decisions

- **Pepper**: Stored as `PASSWORD_PEPPER` in `config/settings.py` — intentionally never stored in the database, so a stolen DB dump can't be brute-forced without the source code.
- **Salt**: Unique per user, generated at registration time, stored alongside the hash. Defeats rainbow table attacks.
- **Custom model**: Uses a standalone `AccountUser` model rather than Django's built-in `User` model — this keeps the database table simple (username, password_hash, salt only) for grading screenshots.
- **Hash**: SHA-256 via `hashlib` (not bcrypt/Argon2) because the project brief explicitly lists it as an example hash function to demonstrate.

I am on Windows 11. Always use cmd.exe commands, never bash or PowerShell commands.

