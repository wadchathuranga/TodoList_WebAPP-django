from django.shortcuts import render, redirect
from .models import Todolist
from .forms import TodolistForm
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    todo_items = Todolist.objects.order_by('id')
    form = TodolistForm()
    context = {'todo_items': todo_items,
               'form': form
               }
    return render(request, 'todolist/index.html', context)


# add todo_item function
@require_POST
def add_todo_item(request):
    form = TodolistForm(request.POST)

    if form.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()

    return redirect('index')


# complete function
def completed_todo(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')


# delete completed
def delete_completed(request):
    Todolist.objects.filter(completed__exact=True).delete()
    return redirect('index')


# delete all
def delete_all(request):
    Todolist.objects.all().delete()
    return redirect('index')