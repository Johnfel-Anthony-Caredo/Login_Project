import os
import django
from django.test import Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import AccountUser

c = Client()
strong_password = 'Cyber@2026Secure'

# Test Registration
response = c.post('/register/', {'username': 'testuser', 'password': strong_password, 'confirm_password': strong_password})
content = response.content.decode()
assert 'Registration Successful' in content, "Registration failed or missing success message"

# Test successful login
response = c.post('/login/', {'username': 'testuser', 'password': strong_password}, follow=True)
content = response.content.decode()
assert 'Login Successful' in content, "Login failed or missing success message"

# Test failed login
response = c.post('/login/', {'username': 'testuser', 'password': 'wrongpassword'})
content = response.content.decode()
assert 'Invalid Username or Password' in content, "Failed login did not show error message"

# Verify DB
user = AccountUser.objects.get(username='testuser')
assert user.salt != "", "Salt should not be empty"
assert user.password_hash != "", "Password hash should not be empty"
assert len(user.password_hash) == 64, "SHA-256 hash should be 64 chars"

print("ALL TESTS PASSED SUCCESSFULLY! ✅")
