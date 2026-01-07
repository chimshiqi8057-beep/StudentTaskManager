# Create your models here.
from django.db import models

class Task(models.Model):
    # 1. Create tasks & 5. Filter by subject
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100) # 存放课程名字
    
    # 2. With deadlines
    deadline = models.DateTimeField()
    
    # 3. Priority levels
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    
    # 4. Mark tasks as complete/pending
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.subject}] {self.title}"