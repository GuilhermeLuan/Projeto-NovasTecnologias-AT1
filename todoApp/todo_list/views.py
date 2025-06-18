from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from .models import todo
from .forms import TodoForm
from django.contrib import messages

@never_cache
def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        if form.is_valid():     
            form.save()
            todos = todo.objects.all()
            return render(request, 'home.html', {'todos': todos} )
    else:
        todos = todo.objects.all()
        return render(request, 'home.html', {'todos': todos} )

def about(request):
    context = {
        "name": "Guilherme Luan",
        "age": 30,
    }
    return render(request, 'about.html', context )

def delete(request, id):
    todos = todo.objects.get(id=id)
    todos.delete()
    messages.success(request, 'Todo deleted successfully!')
    return redirect('home')

def done(request, id):
    todo_item = todo.objects.get(id=id)
    todo_item.isCompleted = True
    todo_item.save()
    messages.success(request, 'Todo marked as completed!')
    print("Todo marked as completed!")
    return redirect('home')

def undone(request, id):
    todo_item = todo.objects.get(id=id)
    todo_item.isCompleted = False
    todo_item.save()
    return redirect('home')