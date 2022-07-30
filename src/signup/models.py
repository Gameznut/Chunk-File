from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

# Create your models here.
class Individual(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ['usename']
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Individual, self).save(*args, **kwargs)

    # def is_anonymous(self, *args, **kwargs):
    #     pass

    # def is_authenticated(self):
    #     return self.username