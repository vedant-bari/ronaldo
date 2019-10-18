from django.urls import path, re_path, include, reverse_lazy

from .views import TodoListView


urlpatterns = [
    path('todolistcreate/',TodoListView.as_view()),
    ]
