from django.db import models
from django.utils.timezone import now

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    reminder_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
