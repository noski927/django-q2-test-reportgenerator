# from django.http import JsonResponse
# from django_q.models import Task


# def task_status(request, task_id):
#     task = Task.object.get(id=task_id)
#     return JsonResponse(
#         {
#             "success": task.success,
#             "result": task.result,
#             "started": task.started,
#             "stopped": task.stopped,
#         }
#     )

from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django_q.tasks import async_task

from .models import UserLog
from .tasks import build_report


@require_http_methods(["GET", "POST"])
def report_page(request, report_id=None):
    if request.method == "POST":
        report = UserLog.objects.create(title="report")
        async_task(build_report, report_id=report.id)
        return redirect("report_page_with_id", report_id=report.id)
    report = None
    if report_id is not None:
        report = get_object_or_404(UserLog, id=report_id)
    return render(request, "reports/page.html")
