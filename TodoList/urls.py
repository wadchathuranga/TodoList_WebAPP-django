from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_todo_item, name='add'),
    path('completed/<todo_id>', views.completed_todo, name='completed'),
    path('deleteCompleted>', views.delete_completed, name='deleteCompleted'),
    path('deleteAll', views.delete_all, name='deleteAll')
]
