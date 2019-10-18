from django.urls import path, re_path, include, reverse_lazy

from .views import SnippetListView


urlpatterns = [
    path('snippet/', SnippetListView.as_view()),
    ]
