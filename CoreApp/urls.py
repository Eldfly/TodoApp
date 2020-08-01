from django.urls import path
from .views import home_view, add_todo, delete_todo


urlpatterns = [
    path('', home_view, name='home'),
    path(r'add_todo/', add_todo, name='add_todo'),
    path(r'delete_todo/<int:todo_id>', delete_todo, name='delete_todo'),

]
