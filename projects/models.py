from django.db import models

# Create your models here.


class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class ApiKey(models.Model):
    key = models.CharField(max_length=40, editable=False, unique=True)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
