import hashlib
import secrets
from django.conf import settings

# ==========================================
# Salt Generation
# Creates a cryptographically secure random 
# hex string for each new user.
# ==========================================
def generate_salt():
    return secrets.token_hex(16)

# ==========================================
# Hashing Implementation & Pepper Usage
# Securely hashes the password using SHA-256 
# by combining it with the salt and the pepper.
# ==========================================
def hash_password(password, salt):
    # Retrieve the pepper constant (hidden in code/settings, NOT in database)
    pepper = settings.PASSWORD_PEPPER
    
    # Combine password + salt + pepper prior to hashing
    combined = password + salt + pepper
    
    # Apply a secure hash function (SHA-256)
    return hashlib.sha256(combined.encode('utf-8')).hexdigest()
