from django.db import models

# Create your models here.
# todo_app/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    def formatted_due_date(self):
        return self.due_date.strftime('%b %d, %Y') if self.due_date else None