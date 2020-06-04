from django.shortcuts import render


from .models import Todo
# Create your views here.


def home_page_view(request):
    todo_items = Todo.objects.all()
    context = {
        'todo': todo_items
    }
    return render(request, "home.html", context)
