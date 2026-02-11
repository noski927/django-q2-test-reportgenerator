from django.db import models
from django.utils import timezone

from polls.enums import UserLogStatuses

USER_LOG_STATUS_CHOICES = [(x.value, x.value) for x in UserLogStatuses]


class UserLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    name = models.CharField(max_length=255, default=None, blank=True, null=True)
    
    c_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=255, choices=USER_LOG_STATUS_CHOICES, default=None, blank=True, null=True)
    task_start_date = models.DateTimeField(default=None, blank=True, null=True)
    task_end_date = models.DateTimeField(default=None, blank=True, null=True)
    progress_percent = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        db_table = "user_logs"
