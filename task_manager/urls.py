from django.contrib import admin
from django.urls import path

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render


tasks = []
complete = []

def task_view(request):
    return render(request, "task.html", {"tasks": tasks})

def add_task_view(request):
    item = request.GET.get("task")
    tasks.append(item)
    return HttpResponse(status=302)

def delete_task_view(request, index):
    del tasks[index-1]
    return HttpResponseRedirect('/task')

def task_viewer(request):
    return render(request, "show.html", {"tasks": tasks})

def complete_task_view(request, index):
    complete.append(tasks.pop(index-1))
    return HttpResponseRedirect('/task')

def view_complete(request):
    return render(request, "complete.html", {"complete": complete})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("task", task_view),
    path("add-task/", add_task_view),
    path("delete-task/<int:index>/", delete_task_view),
    path("tasks/", task_viewer),
    path("complete_task/<int:index>/", complete_task_view),
    path("completed_tasks/", view_complete)
]
