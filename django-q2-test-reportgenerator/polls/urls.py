from django.urls import path

from .views import report_page

urlpatterns = [
    path("report/", report_page, name="report_page"),
    path("report/<int:report_id>/", report_page, name="report_page_with_id"),
]
