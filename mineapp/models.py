from django.db import models
from django.contrib.auth.hashers import make_password

class CreateUser(models.Model):
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    def save(self, *args, **kwargs):
        if not self.pk or 'password' in self.get_dirty_fields():
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    
