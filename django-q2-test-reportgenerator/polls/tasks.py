import traceback
from time import sleep

from .models import Report


def build_report(report_id: int) -> None:
    report = Report.objects.get(id=report_id)
    report.status = Report.Status.RUNNING
    report.save(update_fields=["status"])

    try:
        sleep(15)
        report.status = Report.Status.DONE
        report.save(update_fields=["html", "status"])

    except Exception:
        report.status = Report.Status.FAIL
        report.error = traceback.format_exc()
        report.save(update_fields=["status", "error"])
