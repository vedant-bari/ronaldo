from django.shortcuts import render


##import models
from .models import Snippet
# Create your views here.
from .serializers import SnippetSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class SnippetListView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (AllowAny,)
