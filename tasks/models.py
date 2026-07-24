from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Status(models.TextChoices):
        TODO = "TODO", "To do"
        IN_PROGRESS = "INPROGRESS", "In progress"
        COMPLETED = "COMPLETED", "Completed"

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.TODO
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
