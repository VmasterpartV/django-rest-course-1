from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import Group

from .serializers import GroupSerializer, UserSerializer, DivisionSerializer
from .models import User, Division

# Create your views here.

class GroupView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer