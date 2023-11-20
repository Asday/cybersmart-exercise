from django.urls import include, path, reverse_lazy
from django.views.generic.base import RedirectView

from . import views


app_name = "website"
urlpatterns = [
    path("", views.Tasks.as_view(), name="tasks"),
    path("tasks/", include([
        path("", RedirectView.as_view(url=reverse_lazy("website:tasks"))),
        path("create/", views.TaskCreate.as_view(), name="task_create"),
        path("<int:pk>/", include([
            path("", views.TaskDetail.as_view(), name="task_detail"),
            path("update/", views.TaskUpdate.as_view(), name="task_update"),
        ])),
    ])),
]
