from django.db import models

class Todo(models.Model):
    todo = models.CharField(max_length=255, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
