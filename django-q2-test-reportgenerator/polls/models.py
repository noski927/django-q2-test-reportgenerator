from django.db import models


class Report(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING"
        RUNNING = "RUNNING"
        DONE = "DONE"
        FAIL = "FAIL"

    title = models.CharField(max_length=200, default="title")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    html = models.CharField(blank=True, default="")
    error = models.CharField(blank=True, default="")
