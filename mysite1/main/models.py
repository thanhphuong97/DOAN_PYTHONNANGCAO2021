from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    id = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100)
    created_at = models.DateField(blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True)
    is_admin = models.CharField(max_length=1)
    lastest_login = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'
