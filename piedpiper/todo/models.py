from django.db import models

from piedpiper.users.models import User

class Todo(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    Title = models.TextField()
    text = models.TextField(blank=True, null=True)

