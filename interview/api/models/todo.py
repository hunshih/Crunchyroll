from django.db import models

class Todo(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    completed = models.CharField(max_length=255)