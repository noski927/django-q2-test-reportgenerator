from django.db import models


class UserLog(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING"
        RUNNING = "RUNNING"
        DONE = "DONE"
        FAIL = "FAIL"

    title = models.CharField(max_length=200, default="title")
    c_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    task_start_date = models.DateField(default=None, blank=True, null=True)
    task_end_date = models.DateField(default=None, blank=True, null=True)
    process_percent = models.IntegerField(default=None, blank=True, null=True)
    html = models.CharField(blank=True, default="")
    error = models.CharField(blank=True, default="")
