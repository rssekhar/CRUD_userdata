from django.db import models
from django.forms import PasswordInput

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name) + " " + str(self.email)

    class Meta:
        db_table = 'registerdata'