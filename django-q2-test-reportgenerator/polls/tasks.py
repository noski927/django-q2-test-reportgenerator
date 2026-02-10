import traceback
from time import sleep

from .models import UserLog


def build_report(report_id: int) -> None:
    report = UserLog.objects.get(id=report_id)
    report.status = UserLog.Status.RUNNING
    report.save(update_fields=["status"])

    try:
        sleep(15)
        report.status = UserLog.Status.DONE
        report.save(update_fields=["html", "status"])

    except Exception:
        report.status = UserLog.Status.FAIL
        report.error = traceback.format_exc()
        report.save(update_fields=["status", "error"])
