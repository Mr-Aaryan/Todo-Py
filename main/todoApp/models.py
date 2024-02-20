from django.db import models

class TodoApp(models.Model):
    tasks = models.CharField(max_length = 255)

    def __str__(self):
        return f"{self.tasks}"
