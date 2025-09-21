from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm

def tasks(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

def create(request):
    error = ''
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
            
    form = TasksForm()
    
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'tasks/task-create.html', data)