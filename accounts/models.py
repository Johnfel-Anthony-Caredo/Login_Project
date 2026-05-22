from django.db import models

class AccountUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password_hash = models.CharField(max_length=255)
    salt = models.CharField(max_length=64)

    def __str__(self):
        return self.username
