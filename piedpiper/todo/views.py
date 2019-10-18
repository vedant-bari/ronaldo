from django.shortcuts import render
from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
# Create your views here.

class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    #permission_classes =['AllowAny']
