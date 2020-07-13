from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ChoiceModels(models.Model):
    CHOICES = [
        ('One', 'First choice'),
        ('Two', '2nd choice choice'),
        ('Three', '3rd choice'),
    ]

    choice = models.CharField(max_length=200, choices=CHOICES)