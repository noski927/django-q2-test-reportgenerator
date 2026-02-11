# from django.http import JsonResponse
# from django_q.models import Task

from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, ListView, View
from django_q.tasks import async_task

from .models import UserLog
from .tasks import task_15sec


@require_http_methods(["GET"])
def home_page(request):
    return render(request, "polls/home.html")

@require_http_methods(["POST"])
def create_task_15sec_page(request):
    if request.method == "POST":
        user_log = UserLog.objects.create(name="create_task_15sec")
        async_task(task_15sec, user_log)
        print("create_task_15sec")
        return redirect("polls-user-logs")
    else:
        return HttpResponseBadRequest()

@require_http_methods(["POST"])
def create_10_tasks_15sec_page(request):
    if request.method == "POST":
        for i in range(10):
            print(f"=== create_10_tasks_15sec_page: {i=}")
            user_log = UserLog.objects.create(name="create_task_15sec")
            async_task(task_15sec, user_log)
        return redirect("polls-user-logs")
    else:
        return HttpResponseBadRequest()
    
    
class UserLogListView(ListView):
    model = UserLog
    template_name = "polls/user_log_list.html"
    ordering = ['-c_date']
