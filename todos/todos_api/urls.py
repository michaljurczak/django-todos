from django.urls import path, include

from .views import list_todos, create_todo, update_todo, delete_todo

urlpatterns = [
    path('', list_todos, name='todos_list'),
    path('create/', create_todo, name='create_list'),
    path('update/<int:pk>/', update_todo, name='update_list'),
    path('delete/<int:pk>/', delete_todo, name='delete_list'),
]
