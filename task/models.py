from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    due_time = models.TimeField()
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    CATEGORY = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('other', 'Other'),
    ]
    
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    category = models.CharField(max_length=10, choices=CATEGORY)

    def __str__(self):
        return self.title