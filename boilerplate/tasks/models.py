from django.db import models


class Task(models.Model):
    title = models.CharField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    remind_at = models.DateTimeField()
