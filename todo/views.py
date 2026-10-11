from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home(request):
    if request.method == "POST":
        title = request.POST.get("title")

        if title:
            Task.objects.create(title=title)

        return redirect("home")

    tasks = Task.objects.all().order_by("-created_at")
    remaining_tasks = Task.objects.filter(completed=False).count()

    return render(
        request,
        "todo/home.html",
        {
            "tasks": tasks,
            "remaining_tasks": remaining_tasks,
        }
    )


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()

    return redirect("home")


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()

    return redirect("home")


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        new_title = request.POST.get("title")

        if new_title:
            task.title = new_title
            task.save()

        return redirect("home")

    return render(request, "todo/edit.html", {"task": task})