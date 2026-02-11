from django.urls import path

from .views import home_page, create_task_15sec_page, create_10_tasks_15sec_page, UserLogListView

urlpatterns = [
    path("report/", home_page, name="polls-home"),
    path("polls_create_task_15sec/", create_task_15sec_page, name="polls-create-task-15sec"),
    path("polls_create_10_tasks_15sec/", create_10_tasks_15sec_page, name="polls-create-10-tasks-15sec"),
    path("user_logs/", UserLogListView.as_view(), name="polls-user-logs"),
]
