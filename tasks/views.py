
from django.shortcuts import render, redirect, get_object_or_404

from tasks.models import Task


# views.py

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})



def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})


def task_completion(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if task.completed:
        task.completed = False
    else:
        task.completed = True

    task.save()
    return redirect('task_list')
