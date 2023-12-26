from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)