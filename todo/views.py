from django.shortcuts import render, redirect


from .models import Todo
from .forms import TodoForm
# Create your views here.


def home_page_view(request):
    todo_items = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todo/')
    context = {
        'todo': todo_items,
        'form': form
    }
    return render(request, "home.html", context)


def update_view(request, pk):
    todo_items = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo_items)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo_items)
        if form.is_valid():
            form.save()
        return redirect('/todo')
    context = {
        'form': form
    }
    return render(request, 'update.html', context)


def delete_view(request, pk):
    todo_items = Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo_items.delete()
        return redirect('/todo')
    context = {
        "item": todo_items
    }
    return render(request, 'delete.html', context)
