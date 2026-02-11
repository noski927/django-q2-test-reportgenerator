import traceback
from time import sleep
from django.utils import timezone

from .enums import UserLogStatuses
from .models import UserLog


def task_15sec(user_log: UserLog) -> None:
    user_log.status = UserLogStatuses.Q2_RUNNING.value
    user_log.task_start_date = timezone.now()
    user_log.save()
    
    # sleep(5)
    # user_log.progress_percent = 33
    # user_log.save()
    
    # sleep(5)
    # user_log.progress_percent = 66
    # user_log.save()

    # sleep(5)
    
    total_time = 15
    for i in range(total_time):
        sleep(1)
        user_log.progress_percent = int(100*i/total_time)
        user_log.save()

    user_log.progress_percent = 100
    user_log.task_end_date = timezone.now()
    user_log.status = UserLogStatuses.SUCCESS.value
    user_log.save()
