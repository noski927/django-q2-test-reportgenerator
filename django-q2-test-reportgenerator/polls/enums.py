from enum import Enum


class UserLogStatuses(Enum):
    FAIL = "FAIL"
    PERMISSION_DENIED = "PERMISSION_DENIED"
    SUCCESS = "SUCCESS"
    PENDING = "PENDING"
    Q2_RUNNING = "Q2_RUNNING"
