from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework import permissions

from .models import Reduction
from .serializers import ReductionSerializer

# Create your views here.
class ReductionViewSet(ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ReductionSerializer
    queryset = Reduction.objects.all()
